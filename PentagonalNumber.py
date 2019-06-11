def PentagonalNumber(number):
	x = 1
	
	for i in range(1, number):
		x = x + (5 * i)
		
	return x


print(PentagonalNumber(5))
