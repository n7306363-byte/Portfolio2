import functools
import http.server
import socketserver

DIRECTORY = "/Users/nirmaimon/Desktop/Claude/Projects/Portfolio2"
PORT = 58421

handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=DIRECTORY)

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving {DIRECTORY} at http://localhost:{PORT}")
    httpd.serve_forever()
