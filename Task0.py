for multiple in range(100):
	if multiple % 3 == 0 and multiple  %5 == 0:
		print("FizzBuzz")
		continue
	elif multiple % 3 == 0:
		print("Fizz")
		continue
	elif multiple % 5 == 0:
		print("Buzz")
		continue
	print(multiple)
