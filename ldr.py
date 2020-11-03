#!/usr/bin/env python3
# adapted from a pimoroni example

import time
import explorerhat as hat
threshold = 3.3
while True:
    v = hat.analog.one.read()
    if v < threshold:
            hat.light.green.on()
        else:
            hat.light.green.off()
    print(level)
    time.sleep(0.25)
