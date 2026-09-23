"""Compare recorded, paired human-reviewed runs. Does not invoke or grade models."""
import argparse
from collections import defaultdict
import json
import math
from pathlib import Path


def compare(data):
    if not isinstance(data, dict) or set(data) != {'kind', 'runs'} or data['kind'] not in ('illustrative_synthetic', 'measured'):
        raise ValueError('kind must label synthetic or measured records')
    if not isinstance(data['runs'], list) or not data['runs']:
        raise ValueError('runs must be a nonempty list')
    groups = defaultdict(list)
    seen = set()
    for r in data['runs']:
        if not isinstance(r, dict) or set(r) != {'case_id','strategy','accepted','human_minutes','tokens'}:
            raise ValueError('unexpected run fields')
        if r['strategy'] not in ('solo','roles') or not isinstance(r['case_id'], str) or not r['case_id']:
            raise ValueError('invalid case or strategy')
        key=(r['case_id'],r['strategy'])
        if key in seen: raise ValueError('duplicate case/strategy; use a separate file per repetition')
        seen.add(key)
        if type(r['accepted']) is not bool: raise ValueError('accepted must be bool')
        if type(r['human_minutes']) not in (float,int) or not math.isfinite(r['human_minutes']) or r['human_minutes']<0:
            raise ValueError('invalid minutes')
        if r['tokens'] is not None and (type(r['tokens']) is not int or r['tokens']<0):raise ValueError('invalid tokens')
        groups[r['strategy']].append(r)
    if set(groups) != {'solo','roles'} or {r['case_id'] for r in groups['solo']} != {r['case_id'] for r in groups['roles']}:
        raise ValueError('the same cases must exist in both strategies')
    return {'kind':data['kind'],'not_a_model_benchmark':data['kind']=='illustrative_synthetic','strategies':{
        strategy:{'cases':len(rows),'accepted':sum(r['accepted'] for r in rows),
                  'human_minutes':round(sum(r['human_minutes'] for r in rows),3),
                  'tokens':None if any(r['tokens'] is None for r in rows) else sum(r['tokens'] for r in rows)}
        for strategy,rows in sorted(groups.items())}}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('input',type=Path);args=parser.parse_args()
    try:result=compare(json.loads(args.input.read_text(encoding='utf-8')))
    except (ValueError,OSError,UnicodeError) as exc:parser.exit(2,str(exc)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
