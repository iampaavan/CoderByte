import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
'''
sentence = 'Start a sentence and then bring it to an end'
# pattern = re.compile(r'abc')
#pattern = re.compile(r'coreyms\.com')
# pattern = re.compile(r'.')
#pattern = re.compile(r'\d')
#pattern = re.compile(r'\D')
#pattern = re.compile(r'^Start')
#pattern = re.compile(r'end$')
#pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
#pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
pattern = re.compile(r'[^b]at')
matches = pattern.finditer(text_to_search)
#matches = re.findall(r'[^b]at', text_to_search)

for match in matches:
	print(match)
	#pass

#print(sentence[41:44])

with open('data.txt', 'r', encoding='utf-8') as file_reader:
	contents = file_reader.read()
	
	#matches = pattern.finditer(contents)
	matches = re.findall(r'[8-9]00[-]\d\d\d[-]\d\d\d\d', contents)
	#matches = re.findall(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d', contents)
	part = re.findall(r'[8]00[-][5]55[-]\d\d\d', contents)
	d = dict()
	counter  = 0
	for match in part:
		d[match] = d.get(match, 0) + 1
		counter += 1
		#print(match)
		pass
	#print(d)
	#print(counter)