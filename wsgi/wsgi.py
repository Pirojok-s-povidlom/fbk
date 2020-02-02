#!/usr/bin/env python3
import psycopg2

conn = psycopg2.connect( host="localhost", database="fbk", user="mluzgin", password="mysecretpassword" )
conn.set_session(autocommit=True)

def application(environ, start_response):
    response_body = environ['wsgi.input'].read()
    print(response_body.decode("utf-8"))
    with conn.cursor() as cursor:
        if environ['REQUEST_METHOD'] == 'POST':
            cursor.execute('CREATE TABLE IF NOT EXISTS fbk_data (data varchar(1000) NOT NULL);')
            cursor.execute("INSERT INTO fbk_data(data) VALUES (%s)",[(response_body.decode("utf-8"))] )
        elif environ['REQUEST_METHOD'] == 'GET':
            cursor.execute('SELECT * FROM fbk_data')
            response_body = ''.join(map(str, cursor.fetchall())).encode()
            print(response_body)

    headers = [('Content-Type', 'text/html'),('Content-Length', str(len(response_body)))]

    start_response('200 OK', headers)
    return [response_body]
