#!/usr/bin/env python3

from bottle import route, run
@route('/')
def hello():
    return("hello")

run(host='0.0.0.0', port=8080, debug=True)
