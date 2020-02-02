#!/usr/bin/env python3
import cgitb
import urlparse

cgitb.enable(display=0, logdir="/tmp/test.log")

form = cgi.FieldStorage()

def do_POST(self):
    length = int(self.headers.getheader('content-length'))
    postvars = urlparse.parse_qs(self.rfile.read(length), keep_blank_values=1)
    self.send_response(200)
    self.end_headers()
    self.wfile.write(postvars)


for i in form:
    print(i)
