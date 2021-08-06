def binarySearch(array, target):
    left = 0
	right = len(array) - 1 
	while left <= right:
		middle = (left + right) // 2
		if target == array[middle]:
			return middle # return the index of the matched num
		elif target < array[middle]:
			right = middle - 1
		else: # target > array[middle]:
			left = middle + 1
	return -1 # no number matches
