import http.server
from prometheus_client import start_http_server
from prometheus_client import Counter


REQUESTS = Counter('hello_python_total', 'Hello Pythons requested')

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        REQUESTS.inc()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello Python")

if __name__ == '__main__':
    start_http_server(8000)
    server = http.server.HTTPServer(('localhost', 8001), MyHandler)
    server.serve_forever()