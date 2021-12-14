# j = i each time, and it goes from the end to start of the list
# runs until i hits the end of the list, starts 1 because it will use j-1
# Best: O(n) time, Avg: O(n^2) time, Worst: O(n^2) time. O(1) space in all cases.
def insertionSort(array):
    for i in range(1, len(array)):
		j = i
		while j > 0 and array[j] < array[j - 1]:
			swap(j, j - 1, array)
			j -= 1
	return array

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]
