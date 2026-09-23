#!/usr/bin/python3
import sys

if (len(sys.argv) != 3):
	print("none")
	exit()
print(sys.argv[2].count(sys.argv[1]))