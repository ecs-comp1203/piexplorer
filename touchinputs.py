#!/usr/bin/env python3
# adapted from Pimoroni example
import time
import explorerhat as hat

def touch_cb(channel, event):
    print("{}: {}".format(channel, event))

# what to call if inputs are touched
hat.touch.pressed(touch_cb)
hat.touch.released(touch_cb)
# endless loop - let callbacks do the tasks
while True:
    print("waiting")
    time.sleep(2)
