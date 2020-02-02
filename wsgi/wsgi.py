
#!/usr/bin/env python3
# def application(env, start_response):
#     start_response('200 OK', [('Content-Type','text/html')])
#     return [b"H2ello World"]

import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(
    host="localhost",
    database="fbk",
    user="mluzgin",
    password="mysecretpassword",
)
conn.set_session(autocommit=True)

with conn.cursor() as cursor:
    cursor.execute('CREATE TABLE IF NOT EXISTS fbk_data (data varchar(1000) NOT NULL);')
    value = ['KALA']
    cursor.execute("INSERT INTO fbk_data(data) VALUES (%s)",(value))
    cursor.execute('SELECT * FROM fbk_data LIMIT 10')
    cursor.fetchall()


def application(environ, start_response):
    #response_body = environ['REQUEST_METHOD'].encode('utf-8')
    response_body += environ['wsgi.input'].read()
    status = '200 OK'
    if environ['REQUEST_METHOD'] == 'POST':
        print(environ['wsgi.input'].read())
    print(environ['wsgi.input'].read())
    headers = [('Content-Type', 'text/html'),
            ('Content-Length', str(len(response_body)))]
    start_response(status, headers)
    return [response_body]

# from pprint import pformat
# from cgi import parse_qsl, escape

# def application(environ, start_response):
#     output = '<p>WSGI!</p>'

#     d = parse_qsl(environ['QUERY_STRING'])
#     if environ['REQUEST_METHOD'] == 'POST':
#         output += ('<h1>Post  data:</h1>')
#         output += (pformat(environ['wsgi.input'].read()))

#     if environ['REQUEST_METHOD'] == 'GET':
#         if environ['QUERY_STRING'] != '':
#             output += ('<h1>Get data:</h1>')
#             for ch in d:
#                 output += (' = '.join(ch))
#                 output += ('<br>')

#     output_len = sum(len(line) for line in output)
#     # start_response('200 OK', [('Content-type', 'text/html'),
#     #                           ('Content-Length', str(output_len))])
#     start_response('200 OK', [('Content-Type','text/html')])
#     return [output]
