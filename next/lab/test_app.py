from copy import deepcopy
import io
import json
import threading
import unittest
from unittest.mock import patch, MagicMock
from urllib.request import Request, build_opener, ProxyHandler
from urllib.error import HTTPError, URLError
from core import DEMO_TEXT, DEMO_CARD, InputError, OutputError, clean_text, demo_extract, validate_card
from ollama_client import BackendError, extract, NoRedirect
from server import create_server
from compare_runs import compare


class CoreTests(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(demo_extract(DEMO_TEXT),DEMO_CARD)
    def test_unknowns(self):
        for k in ('meeting_date','participants','join_link'):
            self.assertEqual(demo_extract(DEMO_TEXT)[k],{'value':None,'quote':None})
    def test_changed_demo_rejected(self):
        with self.assertRaises(InputError):demo_extract(DEMO_TEXT+' новое')
    def test_text_boundaries(self):
        for t in ('', '  ', None, 12, 'x'*8001):
            with self.subTest(t=str(t)[:10]), self.assertRaises(InputError):clean_text(t)
    def test_missing_or_extra_keys(self):
        for change in ('missing','extra'):
            x=deepcopy(DEMO_CARD)
            if change=='missing':del x['price_rub']
            else:x['extra']={}
            with self.assertRaises(OutputError):validate_card(x,DEMO_TEXT)
    def test_nonexistent_quote(self):
        x=deepcopy(DEMO_CARD);x['price_rub']['quote']='Стоимость 999.'
        with self.assertRaises(OutputError):validate_card(x,DEMO_TEXT)
    def test_null_pair(self):
        x=deepcopy(DEMO_CARD);x['meeting_date']['quote']='Дату встречи ещё не назначили.'
        with self.assertRaises(OutputError):validate_card(x,DEMO_TEXT)
    def test_bad_value_type(self):
        for v in (True,1200,{},'', 'x'*1001):
            x=deepcopy(DEMO_CARD);x['price_rub']['value']=v
            with self.subTest(value=type(v).__name__),self.assertRaises(OutputError):validate_card(x,DEMO_TEXT)
    def test_no_alias(self):
        x=demo_extract(DEMO_TEXT);x['price_rub']['value']='changed'
        self.assertEqual(demo_extract(DEMO_TEXT)['price_rub']['value'],'1500')
    def test_quote_match_does_not_prove_meaning(self):
        x=deepcopy(DEMO_CARD);x['price_rub']['value']='999999'
        self.assertEqual(validate_card(x,DEMO_TEXT)['price_rub']['value'],'999999')


class AdapterTests(unittest.TestCase):
    def response(self,content):
        m=MagicMock();m.__enter__.return_value.read.return_value=content;return m
    def test_valid_response_and_payload(self):
        opener=MagicMock();opener.open.return_value=self.response(json.dumps({'done':True,'message':{'content':json.dumps(DEMO_CARD)}}).encode())
        with patch('ollama_client.build_opener',return_value=opener):
            self.assertEqual(extract(DEMO_TEXT,'local-test'),DEMO_CARD)
        req=opener.open.call_args.args[0];body=json.loads(req.data)
        self.assertEqual(req.full_url,'http://127.0.0.1:11434/api/chat')
        self.assertIs(body['stream'],False);self.assertIn('properties',body['format'])
    def test_bad_responses(self):
        for raw in (b'not json', b'{}',b'[]',json.dumps({'done':True,'message':{'content':'{}'}}).encode(),b'x'*65537):
            opener=MagicMock();opener.open.return_value=self.response(raw)
            with patch('ollama_client.build_opener',return_value=opener),self.assertRaises(BackendError):extract(DEMO_TEXT,'local-test')
    def test_network_error(self):
        opener=MagicMock();opener.open.side_effect=URLError('test')
        with patch('ollama_client.build_opener',return_value=opener),self.assertRaises(BackendError):extract(DEMO_TEXT,'local-test')
    def test_model_required(self):
        with self.assertRaises(BackendError):extract(DEMO_TEXT,'')
    def test_redirect_rejected(self):
        with self.assertRaises(HTTPError):NoRedirect().redirect_request(Request('http://127.0.0.1:11434'),None,302,'found',{},'https://example.invalid')


class HTTPTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server=create_server(0);cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True);cls.thread.start()
        cls.base='http://127.0.0.1:'+str(cls.server.server_address[1]);cls.opener=build_opener(ProxyHandler({}))
    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown();cls.server.server_close();cls.thread.join()
    def request(self,path,data=None,headers=None):
        h={'Origin':self.base,'Content-Type':'application/json'};h.update(headers or {})
        b=json.dumps(data).encode() if data is not None else None
        req=Request(self.base+path,data=b,headers=h)
        try:
            with self.opener.open(req,timeout=3) as r:return r.status,r.read()
        except HTTPError as e:return e.code,e.read()
    def test_ui_and_no_traversal(self):
        self.assertEqual(self.request('/')[0],200);self.assertEqual(self.request('/../core.py')[0],404)
    def test_demo_http(self):
        code,raw=self.request('/api/extract',{'text':DEMO_TEXT,'mode':'demo'})
        self.assertEqual(code,200);result=json.loads(raw)
        self.assertFalse(result['human_reviewed']);self.assertEqual(len(result['source_sha256']),64)
    def test_wrong_origin(self):
        self.assertEqual(self.request('/api/extract',{'text':DEMO_TEXT,'mode':'demo'},{'Origin':'https://example.invalid'})[0],403)
    def test_invalid_inputs(self):
        for data in ({'text':'','mode':'demo'},{'text':DEMO_TEXT,'mode':'x'},[],{'text':'x'*8001,'mode':'demo'}):
            with self.subTest(data=type(data).__name__):self.assertEqual(self.request('/api/extract',data)[0],400)
    def test_changed_demo(self):
        self.assertEqual(self.request('/api/extract',{'text':'Other note','mode':'demo'})[0],422)
    def test_backend_not_configured(self):
        self.assertEqual(self.request('/api/extract',{'text':DEMO_TEXT,'mode':'ollama'})[0],502)
    def test_wrong_content_type(self):
        self.assertEqual(self.request('/api/extract',{'text':DEMO_TEXT,'mode':'demo'},{'Content-Type':'text/plain'})[0],415)
    def test_busy(self):
        self.server.lesson_lock.acquire()
        try:self.assertEqual(self.request('/api/extract',{'text':DEMO_TEXT,'mode':'demo'})[0],429)
        finally:self.server.lesson_lock.release()


class CompareTests(unittest.TestCase):
    def data(self):
        return {'kind':'measured','runs':[{'case_id':'a','strategy':s,'accepted':True,'human_minutes':1,'tokens':None} for s in ('solo','roles')]}
    def test_valid_unknown_costs(self):
        x=compare(self.data());self.assertIsNone(x['strategies']['solo']['tokens']);self.assertFalse(x['not_a_model_benchmark'])
    def test_mismatched_cases(self):
        d=self.data();d['runs'][1]['case_id']='b'
        with self.assertRaises(ValueError):compare(d)
    def test_duplicate(self):
        d=self.data();d['runs'].append(deepcopy(d['runs'][0]))
        with self.assertRaises(ValueError):compare(d)
    def test_invalid_metrics(self):
        for value in (-1,float('nan'),True):
            d=self.data();d['runs'][0]['human_minutes']=value
            with self.subTest(value=value),self.assertRaises(ValueError):compare(d)
    def test_unknown_kind(self):
        d=self.data();d['kind']='benchmark'
        with self.assertRaises(ValueError):compare(d)


if __name__=='__main__':unittest.main()
