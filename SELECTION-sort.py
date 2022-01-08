# O(N^2) time, O(1) time
# Explanation: sort in place, the left part of the array (in-place) will be sorted (start with the left being len(0))
# Then just find the smallest number on the right side (at the start, it's the whole array), and 
# swap that number with the "currentnum" (the first elem on the right-side array), thus extending the left-hand-side array.
# The very last num, it will already be sorted correctly so stop.
# Ex: [||1, 4, 3] -> [1, || 4, 3] -> [1, 3, || 4] -> [1, 3, 4]  (|| separates LFS and RHS)
def selectionSort(array):
	L = len(array)
	current = 0 # current index
	while current < L - 1: # don't actually go to the last num, since it will be sorted
		smallest = current # index of the smallest num, different with each iteration
		for i in range(current + 1, L): # find the smallest num in the array
			if array[i] < array[smallest]: # we found a new local smallest num
				smallest = i
		# after we found the final smallest number on the unsorted array side, swap it with the num
		# at first, current will be 0, so the num at ind 0 and the smallest will be swapped
		swap(current, smallest, array)
		# current will then be updated, the first number on the right-hand-side array
		current += 1
	return array
				
def swap(p1, p2, array): # swaps two points in an array
	array[p1], array[p2] = array[p2], array[p1]
