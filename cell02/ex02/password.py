password = "Python is awesome"

inp = input()

print("ACCESS GRANTED" if inp[:-1] == password[:-1] else "ACCESS DENIED")