"""Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17"""

my_list = list()


def twoSum(arr, target):
	for i in range(0, len(arr)):
		for j in range(i + 1, len(arr)):
			if (arr[i] + arr[j] == target):
				return True
		
	return False


print(twoSum([1, 2, 4, 5, 7], 9))
print(twoSum([1, 2, 4, 5, 7], 20))

sums = []
hashTable = {}


def summation(array, target):
	for i in range(0, len(array)):
		
		sum_minus_element = target - array[i]
		
		if sum_minus_element in hashTable:
			sums.append([sum_minus_element, array[i]])
		
		hashTable[array[i]] = array[i]
	
	print(hashTable)
	
	return sums


print(summation([1, 2, 4, 5, 7], 9))
