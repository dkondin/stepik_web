def wsgi(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]

    body = environ['QUERY_STRING'][:2].strip().split("&")
    start_response(status, headers)
    return ("\n").join(body)
