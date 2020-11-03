#!/usr/bin/env python3
import time
import explorerhat as hat
from bottle import route, run

@route('/')
def hello():
    return("hello")

@route('/flash')
def flash():
    hat.light.yellow.on()
    time.sleep(0.2)
    hat.light.yellow.off()
    return('flashed')

run(host='0.0.0.0', port=8080, debug=True)
