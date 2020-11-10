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
    print("P.D. across LDR: %sV" % round(5 - v, 3))
    print("LDR resistance: %skΩ" % round(11 * (5 - v) / v, 2))
    time.sleep(0.25)
