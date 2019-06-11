def LetterChanges(string):
	
	new_string = ''
	
	for char in string:
		
		if char.isalpha():
			
			if char.islower() == 'z':
				char = 'a'
				
			else:
				char = chr(ord(char) + 1)
				
		if char in 'aeiou':
			char = char.upper()
			
		new_string = new_string + char
	
	return new_string


print(LetterChanges('fun times!'))
print(f'*******************************************************')
