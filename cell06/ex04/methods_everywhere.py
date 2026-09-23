#!/usr/bin/python3
import sys

def shrink(s: str):
	print(s[0:8])

def enlarge(s: str):
	l = len(s)
	print(s + 'Z' * (7 - l + 1))


if (len(sys.argv) == 1):
	print('none')
else:
	for s in sys.argv[1:]:
		if (len(s) >= 8):
			shrink(s)
		else:
			enlarge(s)

# print(enlarge('7'))
# print(enlarge('66'))
# print(enlarge('555'))
# print(enlarge('4444'))
# print(enlarge('33333'))
# print(enlarge('222222'))
# print(enlarge('1111111'))
# print(enlarge('00000000'))