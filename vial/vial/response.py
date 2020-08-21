import http.client
from .exceptions import ResponseCodeIsInvalid


class Response:

    def __init__(self, data, code=200, content_type='text/html', charset='utf-8'):
        if isinstance(data, (str, bytes)):
            self.data = [data]
        else:
            self.data = data
        try:
            self.http_response = http.client.responses[code]
        except KeyError as e:
            raise ResponseCodeIsInvalid(f'Code {code} is invalid.')
        self.code = code
        self.content_type = content_type
        self.charset = charset
        self.headers = [('Content-Type', f'{self.content_type}; charset={self.charset}')]

    @property
    def status(self):
        return f'{self.code} {self.http_response}'

    @property
    def body(self):
        for row in self.data:
            if isinstance (row, bytes):
                yield row
            else:
                yield row.encode(self.charset)

    def set_headers(self, *args):
        for option in args:
            self.headers.append(option)