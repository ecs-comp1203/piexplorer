#!/usr/bin/env python3
# adapted from a pimoroni example
# if voltage of adc is below a threshold, turn on led
# you need to determine what value to set it to

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
