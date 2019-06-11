def AlphabetSoup(string):
	
	my_list = sorted(list(string), reverse=False)

	return ''.join(my_list)


print(AlphabetSoup('coderbyte'))