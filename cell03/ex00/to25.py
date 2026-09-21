try:
	num = input("Enter a number less than 25\n")
	if int(num) > 25:
		raise ValueError()
	int_num = int(num)
	while int_num <= 25:
		print(f'Inside the loop, my variable is {int_num}')
		int_num += 1
except:
	print("Error")