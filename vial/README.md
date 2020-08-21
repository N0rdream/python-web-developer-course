# Vial

About
----------
Vial is a minimalist WSGI nano web-framework for Python.  

Installation
-----------
```
$ git clone https://github.com/N0rdream/python-web-developer-course.git
$ cd python-web-developer-course/vial
```

Dependencies & requirments
----------

Vial has no dependencies other than the Python Standard Library.  
Vial runs with Python 3.6+.  
To run code examples you’ll need to install uWSGI and curl.  

Examples
-------------
**How to run**
```
uwsgi --http :9090 --wsgi-file example.py --callable app
```
**Import & initialization**

```
from vial.vial import Vial
from vial.response import Response


app = Vial()
```

**Example 1 - Simple 'helloworld'**
```
@app.bind('/hello')
def hello(request):
    return Response(f'<h1>Hello, world!</h1>')
```
Type in browser: http://localhost:9090/hello. 
  
**Example 2 - GET, POST requests handling**
```
@app.bind('/hello/methods')
def hello(request):
    if request.method == 'GET':
        name = request.args_get['name'][0]
        return Response(f'<h1>Hello, {name}!</h1>')
    if request.method == 'POST':
        name = request.args_post['name'][0]
        return Response(f'Hello, {name}!\n', content_type='text/plain')
```
Type in browser: http://localhost:9090/hello/methods?name=GET. 
Type in console: curl -d "name=POST" http://localhost:9090/hello/methods. 
  
**Examples 3 - Customizing headers and status**
```
@app.bind('/hello/headers')
def hello(request):
    response = Response(f'Hello, headers!\n', code=202, content_type='text/plain')
    response.set_headers(('foo', '42'), ('bar', 'baz'))
    return response
```
Type in console: curl -v http://localhost:9090/hello/headers. 
  
Notes
-----------
Vial is written for reinventing wheel purpose.  
Vial does not support POST requests with 'multipart/form-data' content type.  