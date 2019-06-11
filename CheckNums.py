def CheckNums(number1, number2):
	
	if number1 == number2:
		return -1
	
	elif number2 > number1:
		return True
	
	else:
		return False
	

print(CheckNums(3, 122))
print(f'*****************************************************')
print(CheckNums(120, 5))
print(f'*****************************************************')
print(CheckNums(10, 10))
print(f'*****************************************************')
