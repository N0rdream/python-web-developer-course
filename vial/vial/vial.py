from .response import Response
from .request import Request


class Vial:

    def __init__(self):
        self.routes = {}

    def bind(self, path):
        def wrapper(func):
            self.routes[path] = func
        return wrapper

    def return_view(self, path):
        try:
            return self.routes[path]
        except KeyError:
            return None

    def __call__(self, environ, start_response):
        request = Request(environ)
        if request.is_multipart():
            response = Response(f'<h1>Error 501. Not implemented</h1>', 501)
            start_response(response.status, response.headers)
            return response.body
        func = self.return_view(request.path)
        if func is None:
            response = Response(f'<h1>Error 404. Not found: {request.path}</h1>', 404)
        else:
            response = func(request)
        start_response(response.status, response.headers)
        return response.body