import operator, re, os


def wordfrequency(string):
	my_list = string.split(" ")
	d = {}
	for i in my_list:
		d[i] = d.get(i, 0) + 1
	
	sorted_dict = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
	return sorted_dict


print(wordfrequency('hello world program world test test test program'))


def word_count_file(filename):
	os.chdir('C:\\Users\\Paavan Gopala\\Downloads')
	d = dict()
	with open(filename, 'r') as file_reader:
		contents = file_reader.read()
		# match_pattern = re.findall(r'\b[a-z]{3,15}\b', contents)
		match_pattern = re.findall(r'\b[a-z]{3,15}\b', contents)
		
		for word in match_pattern:
			d[word] = d.get(word, 0) + 1
			
		sorted_dict = sorted(d.items(), key=operator.itemgetter(1))
			
		return sorted_dict
	
	
print(word_count_file('test.txt'))
