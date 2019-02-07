#!/usr/bin/env python3

import os
import json
# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))

#import bottle
from bottle import route, default_app, template, get, post, request, static_file
# ... build or import your bottle application here ...
# Do NOT use bottle.run() with mod_wsgi

index_html = '''My first web app! By <strong>{{ author }}</strong>.'''

@get('/hello') # or @route('/hello')
def hello():
    return '''
        <form action="/hello" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''
    # return "Hello World!"

@post('/hello')
def returnInfo():
    username = request.forms.get('username')
    password = request.forms.get('password')
    return '<p>login info entered.</p>'

html_string = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My App</title>
    <link rel="stylesheet" type="text/css" href="reset.css">
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
<div class="sidenav">
 <form action="/" method="post">
  <!--First name:<br>-->
     <select name="genres">
         <option value="sci-fi">Sci Fi</option>
         <option value="drama">Drama</option>
     </select>
     <input type="text" name="year" value="">
     <input id="submit" type="button" value="Submit">
</form>

</div>
<!--<h1>hello</h1>-->
<div class="main">
    <p>hello</p>
</div>
<script src="aja.js"></script>
<script src="myscript.js"></script>
</body>
</html>
'''

@route('/<filename:re:.*\.css>')
def send_static(filename):
    return static_file(filename, root='css/')

@route('/<filename:re:.*\.js>')
def send_static(filename):
    return static_file(filename, root='js/')

@route('/')
def home():
    return html_string
    # return static_file("", root='/index.html')
    # return template(index_html, author='vivek')
    # return 'this is home.'


@post('/')
def form():
    val1 = request.forms.get('val1')
    val2 = request.forms.get('val2')
    return json.dumps({'val1': val1, 'val2': val2})
    # return '<p>login info entered.</p>'


application = default_app()

