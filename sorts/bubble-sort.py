# this way of doing bubble sort: go through the array comparing two adjacent numbers, moving them by 1 index
#then decrease the size of the array you're looking at each time. Since BubSort is moving the biggest number to the end each time.
# O(n^2) time, O(1) space
def bubbleSort(array):
	n = len(array)
	if n < 2: # edge case
		return array
    for s in range(n - 1):
		for i in range(1, n - s):
			if array[i] < array[i - 1]:
				array[i], array[i - 1] = array[i - 1], array[i] # swap them
		#for j in range()
	return array
