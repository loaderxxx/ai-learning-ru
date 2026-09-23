"""Local educational web app. Not a production/multi-user server."""
import argparse
from hashlib import sha256
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import threading
from time import perf_counter
from core import LABELS, DEMO_TEXT, InputError, clean_text, demo_extract
from ollama_client import BackendError, extract

ROOT = Path(__file__).resolve().parent
STATIC = {'/': ('index.html', 'text/html; charset=utf-8'),
          '/app.js': ('app.js', 'text/javascript; charset=utf-8'),
          '/style.css': ('style.css', 'text/css; charset=utf-8')}


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass  # Do not log note bodies, prompt contents or access query strings.

    def setup(self):
        super().setup()
        self.connection.settimeout(5)

    def send(self, status, payload, content_type='application/json; charset=utf-8'):
        body = payload if isinstance(payload, bytes) else json.dumps(payload, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; object-src 'none'; frame-ancestors 'none'; base-uri 'none'")
        self.end_headers()
        self.wfile.write(body)

    def valid_host(self):
        port = self.server.server_address[1]
        return self.headers.get('Host') in (f'127.0.0.1:{port}', f'localhost:{port}')

    def do_GET(self):
        if not self.valid_host():
            return self.send(403, {'error': 'Откройте приложение по локальному адресу.'})
        if self.path in STATIC:
            name, kind = STATIC[self.path]
            return self.send(200, (ROOT / name).read_bytes(), kind)
        if self.path == '/api/example':
            return self.send(200, {'text': DEMO_TEXT})
        if self.path == '/api/meta':
            return self.send(200, {'labels': LABELS, 'model': self.server.lesson_model,
                                   'ollama_endpoint': 'http://127.0.0.1:11434/api/chat'})
        self.send(404, {'error': 'Страница не найдена.'})

    def do_POST(self):
        origin = self.headers.get('Origin')
        if not self.valid_host() or origin != 'http://' + self.headers.get('Host', ''):
            return self.send(403, {'error': 'Запрос должен исходить из локального интерфейса.'})
        if self.path != '/api/extract':
            return self.send(404, {'error': 'Неизвестное действие.'})
        if self.headers.get('Content-Type', '').split(';')[0] != 'application/json' or self.headers.get('Transfer-Encoding'):
            return self.send(415, {'error': 'Нужен обычный JSON-запрос.'})
        try:
            size = int(self.headers.get('Content-Length', '0'))
            if not 0 < size <= 32768:
                return self.send(413, {'error': 'Запрос слишком большой или пустой.'})
            raw = self.rfile.read(size)
            if len(raw) != size:
                raise ValueError('incomplete')
            data = json.loads(raw)
            if not isinstance(data, dict) or set(data) != {'text', 'mode'}:
                raise InputError('Некорректные поля запроса.')
            text = clean_text(data['text'])
            if data['mode'] not in ('demo', 'ollama'):
                raise InputError('Неизвестный режим.')
        except (ValueError, UnicodeError, TimeoutError):
            return self.send(400, {'error': 'Проверьте запрос: непустой текст до 8000 символов и известный режим.'})
        if not self.server.lesson_lock.acquire(blocking=False):
            return self.send(429, {'error': 'Одна обработка уже идёт. Дождитесь её окончания.'})
        try:
            started = perf_counter()
            card = demo_extract(text) if data['mode'] == 'demo' else extract(text, self.server.lesson_model, self.server.lesson_timeout)
            self.send(200, {'card': card, 'mode': data['mode'],
                           'model': None if data['mode'] == 'demo' else self.server.lesson_model,
                           'seconds': round(perf_counter() - started, 3),
                           'source_sha256': sha256(text.encode()).hexdigest(),
                           'human_reviewed': False, 'source_text': text})
        except InputError as exc:
            self.send(422, {'error': str(exc)})
        except BackendError as exc:
            self.send(502, {'error': str(exc)})
        finally:
            self.server.lesson_lock.release()


def create_server(port=8765, model='', timeout=60):
    server = ThreadingHTTPServer(('127.0.0.1', port), Handler)
    server.lesson_model = model
    server.lesson_timeout = timeout
    server.lesson_lock = threading.Lock()
    return server


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8765)
    parser.add_argument('--model', default='')
    parser.add_argument('--timeout', type=int, default=60)
    args = parser.parse_args()
    if not 1 <= args.port <= 65535 or not 1 <= args.timeout <= 300:
        parser.error('port: 1..65535; timeout: 1..300')
    with create_server(args.port, args.model, args.timeout) as server:
        print(f'Откройте http://127.0.0.1:{args.port} — остановка Ctrl+C', flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
