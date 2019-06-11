def SimpleSymbols(string):
	
	string = '=' + string + '='
	print(string)
	for i in range(0, len(string)):
		
		if string[i].isalpha():

			if string[i - 1] != '+' or string[i + 1] != '+':
				
				return False
			
	return True


print(SimpleSymbols('f++d+'))
print(f'****************************************************')
print(SimpleSymbols('+d+=3=+s+'))
