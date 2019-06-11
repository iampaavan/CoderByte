"""Given an array of integers, return a new array such that each element at index i of the new array
is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6]."""


def new_array(array):
	product = 1
	my_list = []
	for i in range(0, len(array)):
		for j in range(0, len(array)):
			if i != j:
				product = product * array[j]
			
		my_list.append(product)
		product = 1
	return my_list


print(new_array([1, 2, 3, 4, 5]))
print(f'********************************************')
print(new_array([3, 2, 1]))


