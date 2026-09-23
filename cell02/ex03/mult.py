#!/usr/bin/python3
first_num = input("Enter the first number: \n")
second_num = input("Enter the second number: \n")

mul = int(first_num) * int(second_num)
print(f'{first_num} x {second_num} = {mul}')
print("The result is positive." if mul > 0 else "The result is positive and negative." if mul == 0 else "The result is negative.")