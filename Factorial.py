"""Method - 1"""


def factorial(number):
	
	if number == 1:
		return 1

	elif number == 0:
		return 1
	
	else:
		return number * factorial(number - 1)
	
	
print(factorial(4))
print(factorial(0))

"""Method - 2"""


def first_factorial(number):
	"""return the factorial of a number"""
	factorial = 1
	
	for i in range(1, number + 1):
		factorial = factorial * i
	
	return factorial


print(first_factorial(10))
