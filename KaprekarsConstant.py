def KaprekarsConstant(number):

	counter = 0
	maths = 0
	flag = True

	while flag:
		
		if len(str(number)) < 4:
				number = str(number).zfill(4)
				
		number = str(number)
		my_list_dec = sorted(list(number), reverse=True)
		my_list_asc = sorted(list(number), reverse=False)
		str_dec = int(''.join(my_list_dec))
		str_asc = int(''.join(my_list_asc))
		
		maths = str_dec - str_asc
		if maths == 6174:
			flag = False
		counter += 1
		number = maths
	print(maths)
	print(counter)


KaprekarsConstant(9831)
KaprekarsConstant(3524)
KaprekarsConstant(2324)
KaprekarsConstant(2111)
KaprekarsConstant(1000)
KaprekarsConstant(1112)
KaprekarsConstant(9812)


def zero(number):
	if len(str(number)) < 4:
		number = str(number).zfill(4)
	
	return number


print(zero(23))
