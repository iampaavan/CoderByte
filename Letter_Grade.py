print(f'Welcome to GPA Calculator')
print(f'Please enter all your letter grades, one per line:')
print(f'Enter a blank line to designate the end.')

total_courses = 0
total_points = 0
flag = True

points = {'A+': 4.0, 'A': 4.0, 'A-': 3.67, 'B+': 3.33, 'B': 3.0, 'B-': 2.67,
'C+': 2.33, 'C-': 2.0, 'C': 1.67, 'D+': 1.33, 'D': 1.0, 'F': 0.0}

while flag:
	grade = input(f'Enter your letter grade:')
	
	if grade == '':
		flag = False
		
	elif grade not in points:
		print(f"Unknown grade {grade}. It is ignored. Won't be counted towards your total points.")
		
	else:
		total_points += 1
		total_courses += points[grade]
		
	if total_courses > 0 and total_points > 0:
		try:
			print(f'Your current GPA is: {total_courses/total_points}')
			
		except ZeroDivisionError:
			print(f'Total points cannot be zero.')
			
	else:
		print(f'Your GPA is 0')