#!/usr/bin/python3
import sys


if (len(sys.argv) == 2):
	cnt = sys.argv[1].count('z') 
	print('z' * cnt if cnt > 0 else "none")
	exit()
print("none")