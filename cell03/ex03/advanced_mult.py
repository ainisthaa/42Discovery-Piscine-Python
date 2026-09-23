#!/usr/bin/python3
import sys

if (len(sys.argv) != 1):
	print("none")
	exit()

for i in range(11):
	print(f'Table de {i}: {" ".join(map(str, [i * j for j in range(11)]))}')
	