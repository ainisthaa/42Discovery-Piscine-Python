#!/usr/bin/python3
import sys

l = len(sys.argv)

if (l == 1):
	print("none")
else:
	print(f"parameters: {l - 1}")
	for i in range(1, l):
		print(f"{sys.argv[i]}: {len(sys.argv[i])}")