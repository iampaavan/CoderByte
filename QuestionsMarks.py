def QuestionsMarks(s):
	a, b = 0, 0
	for i in range(0, len(s)-1):
		for j in range(i, len(s)-1):
			if s[i].isdigit() and s[j].isdigit() and int(s[i]) + int(s[j]) == 10:
				a, b = i, j
	new = s[a:b+1]
	print(new)
	if new.count('?') == 3:
		return 'true'
	else:
		return 'false'

	
#print(QuestionsMarks('aa6?9'))
#print(QuestionsMarks('acc?7??sss?3rr1??????5'))


def quesmark(str):
	a, b = 0, 0
	for i in range(0, len(str) - 1):
		for j in range(i, len(str) - 1):
			if str[i].isdigit() and str[j].isdigit() and int(str[i]) + int(str[j]) == 10:
				a, b = i, j
	
	new = str[a: b+1]
	if new.count('?') == 3:
		return True
	else:
		return False


print(quesmark('acc?7??sss?3rr1??????5'))
