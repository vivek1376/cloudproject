#!/usr/bin/env python3

import os
import json
import requests

api_key='0ebba73bf032314a5c9ff1de0e692f60'
# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))

#import bottle
from bottle import route, default_app, template, get, post, request, static_file, response, debug
# ... build or import your bottle application here ...
# Do NOT use bottle.run() with mod_wsgi

# index_html = '''My first web app! By <strong>{{ author }}</strong>.'''

@get('/hello') # or @route('/hello')
def hello():
    response.content_type = 'application/json'
    # return json.dumps({'a':'b'})
    return json.dumps(tmdb_api_call())

    # return '''
    #     <form action="/hello" method="post">
    #         Username: <input name="username" type="text" />
    #         Password: <input name="password" type="password" />
    #         <input value="Login" type="submit" />
    #     </form>
    # '''
    # return "Hello World!"


def tmdb_api_call():
    fetch_genres_url = 'https://api.themoviedb.org/3/genre/movie/list?api_key=' + api_key + '&language=en-US'
    resp_genres = requests.get(fetch_genres_url)
    resp_genres_json = resp_genres.json()
    return resp_genres_json


def tmdb_api_get_movies_list(genreid, releaseyr):
    fetch_movies_url = 'https://api.themoviedb.org/3/discover/movie?api_key=' + api_key \
    + '&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&' \
      'page=1&primary_release_year=' + str(releaseyr) + '&with_genres=' + str(genreid) \
    + '&with_original_language=en'

    movies_list = requests.get(fetch_movies_url)
    movies_list_json = movies_list.json()
    return movies_list_json


def get_select_opts_genre():
    api_key = '0ebba73bf032314a5c9ff1de0e692f60'
    fetch_genres_url = 'https://api.themoviedb.org/3/genre/movie/list?api_key=' + api_key + '&language=en-US'
    resp_genres = requests.get(fetch_genres_url)
    resp_genres_json = resp_genres.json()

    opts_str = ''

    for e in resp_genres_json['genres']:
        opts_str += ('<option value="' + str(e['id']) + '">' + e['name'] + '</option>')

    return opts_str


@post('/hello')
def returnInfo():
    # return json.dumps(tmdb_api_call())
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

    return template(html_string, select_opts=get_select_opts_genre()) # , hello_name='vivek')

    # return html_string

    # return static_file('index.html', root='/')
    # return html_string

    # return static_file("", root='/index.html')
    # return template(index_html, author='vivek')
    # return 'this is home.'


@post('/')
def form():
    genreid = request.forms.get('genreid')
    releaseyr = request.forms.get('relyear')

    return tmdb_api_get_movies_list(genreid, releaseyr)
    # return json.dumps({'val1': val1, 'val2': val2})
    # return '<p>login info entered.</p>'

debug(mode=True)
application = default_app()

#

