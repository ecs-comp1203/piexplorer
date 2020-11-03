#!/usr/bin/env python3

import time
import explorerhat
touched = [False] * 8


def ohai(channel, event):
    touched[channel - 1] = True
    print("{}: {}".format(channel, event))

# what to call if ainputs are touched
explorerhat.touch.pressed(ohai)
explorerhat.touch.released(ohai)

input_status = False

while True:
    print("waiting")
    time.sleep(2)

explorerhat.pause()
