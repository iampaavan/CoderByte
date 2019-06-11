import math


def TimeConvert(time):
	
	hours = int(math.floor(time / 60))
	minutes = math.floor(time % 60)
	
	return str(hours) + ':' + str(minutes)


print(TimeConvert(126))
print(f'**********************************************************')
print(TimeConvert(45))