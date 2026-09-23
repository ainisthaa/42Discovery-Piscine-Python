#!/usr/bin/python3
def is_int(n):
	try:
		int(n)
		return (True)
	except ValueError:
		return (False)
	
def is_float(n):
	try:
		float(n)
		return(True)
	except ValueError:
		return (False)


n = str(input("Give me a number: "))
if (is_int(n) or (is_float(n) and (float(n) == int(float(n))))):
	print("This number is an integer.")
elif (is_float(n)):
	print("This number is a decimal.")
else:
	print("this program take only numberic idiot !")