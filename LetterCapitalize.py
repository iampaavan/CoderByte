def LetterCapitalize(string):
	return string.title()


print(LetterCapitalize('hello world'))
print(f'*************************************************')
print(LetterCapitalize('i ran there'))


def LetterCaptial(str):
	
	words = str.split(" ")
	
	for i in range(0, len(words)):
		words[i] = words[i][0].upper() + words[i][1:]
		
	return " ".join(words)


print(f'************************************************')
print(LetterCaptial('hello world'))
print(f'************************************************')
print(LetterCaptial('i ran there'))
