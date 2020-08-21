from vial.vial import Vial
from vial.response import Response


app = Vial()

# type in browser: http://localhost:9090/hello
@app.bind('/hello')
def hello(request):
    return Response(f'<h1>Hello, world!</h1>')

# type in browser: http://localhost:9090/hello/methods?name=GET
# type in console: curl -d "?name=POST" http://localhost:9090/hello/methods
@app.bind('/hello/methods')
def hello(request):
    if request.method == 'GET':
        name = request.args_get['name'][0]
        return Response(f'<h1>Hello, {name}!</h1>')
    if request.method == 'POST':
        name = request.args_post['name'][0]
        return Response(f'Hello, {name}!\n', content_type='text/plain')

# type in console: curl -v http://localhost:9090/hello/headers
@app.bind('/hello/headers')
def hello(request):
    response = Response(f'Hello, headers!\n', code=2002, content_type='text/plain')
    response.set_headers(('foo', '42'), ('bar', 'baz'))
    return response