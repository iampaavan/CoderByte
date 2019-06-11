my_list = list()


def twoSum(arr, target):
	
	for i in range(0, len(arr)):
		for j in range(i + 1, len(arr)):
			if (arr[i] + arr[j] == target):
				my_list.append([i, j])
				
	return my_list


print(twoSum([1, 2, 4, 5, 7], 9))


sums = []
hashTable = {}


def summation(array, target):
	
	for i in range(0, len(array)):
		
		sum_minus_element = target - array[i]
		
		if sum_minus_element in hashTable:
			sums.append([sum_minus_element, array[i]])
			
		hashTable[array[i]] = array[i]
		
	return sums


print(summation([1, 2, 4, 5, 7], 9))
