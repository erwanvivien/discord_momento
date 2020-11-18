import http.server
import socketserver
import os
from threading import Thread

PORT = os.environ.get("PORT") or 8000
PORT = int(PORT)

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)


def start_server():
    httpd.serve_forever()


t = Thread(target=start_server)
t.start()

while True:
    import cron
    import time
    cron.main()
    time.sleep(60 * 10)
