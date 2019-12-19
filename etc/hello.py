def wsgi(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]

    body = environ['QUERY_STRING'].strip().split("&")
    start_response(status, headers)
    return [el + "\n" for el in body]
