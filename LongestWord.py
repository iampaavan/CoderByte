def LongestWord(sen):
	
	sen = sen.translate(sen.maketrans('', '', "~!@#$%^&*()-_+={}[]:;'<>?/,.|`"))
	arr = sen.split(" ")
	
	return max(arr, key=len)


print(LongestWord("fun&!! time"))
print('***********************************************************************')
print(LongestWord('I love dogs'))


