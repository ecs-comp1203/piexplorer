#!/usr/bin/env python3
# print the CPU temperature, having paresed it from the wierd string
# extracts the number as a float
import os
import subprocess as sub

result = sub.run(["vcgencmd","measure_temp"], capture_output=True)
tempstring = str(result.stdout)
temp = float(tempstring.split("=")[1].split("'")[0])
print(temp)
