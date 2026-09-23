#!/usr/bin/python3
import sys

if (len(sys.argv) != 3):
	print("none")
else:
	end = int(sys.argv[2])
	print(list(range(int(sys.argv[1]), end)) + [end])