inp = input()
try:
    num = int(inp)
except ValueError:
    print("InputError: only numbers")
    exit()


print("This number is positive." if num > 0 else "This number is negative." if num < 0 else "This number is both positive and negative.")