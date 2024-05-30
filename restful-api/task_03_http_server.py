#!/usr/bin/python3
from http.server import HTTPServer, BaseHTTPRequestHandler


class Subclass(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header()
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")
        
        
httpd = HTTPServer(('', 8000), Subclass)
httpd.serve_forever()
