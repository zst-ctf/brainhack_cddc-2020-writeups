#!/usr/bin/env python
import time
from calendar import timegm

def convert(s):
	utc_time = time.strptime(s, "%Y.%m.%d %H:%M:%S")
	epoch_time = timegm(utc_time)
	return epoch_time

dates = '''2005.10.06 05:23:15
2020.10.05 22:39:46
2020.08.29 05:16:57
2020.08.12 10:05:39
2020.09.29 06:36:38
2020.09.27 00:41:56
2020.09.30 18:43:24
2020.08.10 03:54:13
2020.09.24 00:09:37
2020.09.16 09:20:23
2020.08.10 22:06:44
2020.08.10 23:19:09
2020.08.13 22:08:52
1987.04.11 00:43:13'''.splitlines()

prev = 0
for d in dates:
	current = convert(d)
	delta = current - prev
	print(current, delta, hex(current), hex(delta))
	prev = current