#!/usr/bin/python3
def greetings(s = "noble stranger."):
	try:
		print("Hello, " + s)
	except TypeError:
		print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)