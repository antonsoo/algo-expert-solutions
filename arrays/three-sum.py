# problem: find all triplets of three numbers in the array that add up to our target sum and return those triplets of numbers 
# solution:
# sort the array to make things easier and to know how to move towards the correct sum
# have three pointers, keep one pointer constant through a for loop, and move two others L and R
# move them based on where the position towards our target sum is closer 
# O(N^2) time, O(N) space for the output array
def threeNumberSum(array, targetSum): # assume array is n >= 3
	array.sort() # sort in place
	output = []
	for ind, num in enumerate(array): # goes through the entire array
		if ind >= len(array) - 2: # terminate if it gets too big to not get out of bounds
			break
		# initialize R and L
		L = ind + 1 # right after the current i pointer
		R = len(array) - 1 # the end of the list
		while L < R: # while strictly smaller
			currsum = num + array[L] + array[R]
			if targetSum == currsum: # matches
				output.append([num, array[L], array[R]])
				L += 1
				R -= 1
			# else, move it in the direction towards the numbers to get our targetSum
			elif currsum < targetSum:
				L += 1 
			elif currsum > targetSum:
				R -= 1
	return output
