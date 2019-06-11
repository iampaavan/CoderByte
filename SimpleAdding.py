def SimpleAdding(number):
	sum = 0
	
	for i in range(1, number + 1):
		sum = sum + i
		
	return sum


print(SimpleAdding(4))
print(f'*************************************')
print(SimpleAdding(12))
print(f'*************************************')
print(SimpleAdding(140))
print('**************************************')


def alternate(num):
	return int(num * ((num + 1) / 2))


print(alternate(4))
print(f'************************************')
print(alternate(12))
print(f'************************************')
print(alternate(140))

