#!/usr/bin/env python3
import time
import explorerhat as hat
from bottle import route, run
import subprocess as sub

@route('/')
def hello():
    return("hello")

@route('/flash')
def flash():
    hat.light.yellow.on()
    time.sleep(0.2)
    hat.light.yellow.off()
    return('flashed')

@route('/cputemp')
def index(name='cputemp'):
    result = sub.run(["vcgencmd","measure_temp"], capture_output=True)
    return(result.stdout)

run(host='0.0.0.0', port=8080, debug=True)
