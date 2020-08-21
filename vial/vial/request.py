from urllib.parse import parse_qs


class Request:

    def __init__(self, environ):
        self.environ = environ

    @property
    def args_get(self):
        return parse_qs(self.environ.get('QUERY_STRING'))

    @property
    def method(self):
        return self.environ.get('REQUEST_METHOD')

    @property
    def path(self):
        return self.environ.get('PATH_INFO')
    
    @property
    def content_length(self):
        return int(self.environ.get('CONTENT_LENGTH'))

    @property
    def content_type(self):
        return self.environ.get('CONTENT_TYPE')

    @property
    def post_data(self):
        return self.environ.get('wsgi.input')

    @property
    def args_post(self):
        return parse_qs(self.post_data.read(self.content_length).decode())

    def is_multipart(self):
        if self.method == 'POST':
            if self.content_type.startswith('multipart/'):
                return True