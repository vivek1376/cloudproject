#!/usr/bin/env python3

import os
import json
# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))

#import bottle
from bottle import route, default_app, template, get, post, request, static_file
# ... build or import your bottle application here ...
# Do NOT use bottle.run() with mod_wsgi

# index_html = '''My first web app! By <strong>{{ author }}</strong>.'''

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


@route('/<filename:re:.*\.css>')
def send_static(filename):
    return static_file(filename, root='css/')

@route('/<filename:re:.*\.js>')
def send_static(filename):
    return static_file(filename, root='js/')

@route('/')
def home():
    with open('index.html', 'r') as myfile:
        html_string = myfile.read()

    return html_string

    # return static_file('index.html', root='/')
    # return html_string

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

