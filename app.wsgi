#!/usr/bin/env python3

import os
import json
import requests

api_key = '0ebba73bf032314a5c9ff1de0e692f60'

# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))

# import bottle
from bottle import route, default_app, template, get, post, request, static_file, response, debug


def tmdb_api_get_movies_list(genreid, releaseyr):
    fetch_movies_url = 'https://api.themoviedb.org/3/discover/movie?api_key=' + api_key \
                       + '&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&' \
                         'page=1&primary_release_year=' + str(releaseyr) + '&with_genres=' + str(genreid) \
                       + '&with_original_language=en'

    movies_list = requests.get(fetch_movies_url)
    movies_list_json = movies_list.json()

    items = movies_list_json['results']

    # create empty dict
    movieList_dict = {}

    movieList_dict['status'] = 'ok'
    movieList_dict['list'] = []

    for item in items:
        movieID = item['id']
        movieTitle = item['title']
        movieOverview = item['overview']

        # make api call to fetch movie detail, imdb id and poster path
        fetch_movie_detail_url = 'https://api.themoviedb.org/3/movie/' + str(movieID) + '?api_key=' \
                                 + api_key + '&language=en-US'

        movie_detail_resp = requests.get(fetch_movie_detail_url)
        movie_detail_resp_json = movie_detail_resp.json()
        movie_imdbID = movie_detail_resp_json['imdb_id']
        movie_posterID = movie_detail_resp_json['poster_path']

        movieList_dict['list'].append({'id': movieID,
                                       'title': movieTitle,
                                       'overview': movieOverview,
                                       'imdbid': movie_imdbID,
                                       'posterid': movie_posterID})

    response.content_type = 'application/json'
    return json.dumps(movieList_dict)


def get_select_opts_genre():
    api_key = '0ebba73bf032314a5c9ff1de0e692f60'
    fetch_genres_url = 'https://api.themoviedb.org/3/genre/movie/list?api_key=' + api_key + '&language=en-US'
    resp_genres = requests.get(fetch_genres_url)
    resp_genres_json = resp_genres.json()

    opts_str = ''

    for e in resp_genres_json['genres']:
        opts_str += ('<option value="' + str(e['id']) + '">' + e['name'] + '</option>')

    return opts_str


@route('/<filename:re:.*\.css>')
def send_static(filename):
    return static_file(filename, root='css/')


@route('/<filename:re:.*\.js>')
def send_static(filename):
    return static_file(filename, root='js/')


@route('/<filename:re:.*\.png>')
def send_static(filename):
    return static_file(filename, root='static/')


@route('/')
def home():
    with open('index.html', 'r') as myfile:
        html_string = myfile.read()

    return template(html_string, select_opts=get_select_opts_genre())


@post('/')
def form():
    genreid = request.forms.get('genreid')
    releaseyr = request.forms.get('relyear')

    return tmdb_api_get_movies_list(genreid, releaseyr)


# debug(mode=True)
application = default_app()
