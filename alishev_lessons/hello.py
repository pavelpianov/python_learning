#!/usr/bin/env python3

from threading import Timer

# sieve = [True] * 101
# for i in range(2, 100):
# 	if sieve[i]:
# 		print(i)
# 		for j in range(i*i, 100, i):
# 			sieve[j] = False

msg = "Hello World!"
print(msg)
# Timer(4.0, print, msg).start()
Timer(4.0, exit).start()