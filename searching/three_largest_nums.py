"""
problem: find the three largest numbers
solution: have a deque that stores the three current largest numbers and rotate or change the numbers as needed (inspired by a LC ans)
complexity: O(n) time, O(1) space
"""
from collections import deque
def findThreeLargestNumbers(array):	
    ans = deque([-float('inf')] * 3) # initialize to lowest numbers possible
	print(ans)
	# go through array and compare that number to ans array
	for num in array:
		if num > ans[2]:
			ans.rotate(-1)
			ans[2] = num
		elif num > ans[1]:
			ans[0] = ans[1]
			ans[1] = num
		elif num > ans[0]:
			ans[0] = num
	return list(ans)

#-------------------------------------

# Official solution, no rotation or shift used explicitely. Instead we define it by ourselves.
#also O(N) time and O(1) space.
def findThreeLargestNumbers(array):
    threeLargest = [None, None, None] # can also make this float('-inf')
	for num in array:
		updateLargest(threeLargest, num) # helperfunc
	return threeLargest

def updateLargest(threeLargest, num):
	# if it's larger than the largest number
	if threeLargest[2] is None or num > threeLargest[2]:
		shiftAndUpdate(threeLargest, num, 2) # 2 is the index
	elif threeLargest[1] is None or num > threeLargest[1]:
		shiftAndUpdate(threeLargest, num, 1) # 1'th index; the middle number
	elif threeLargest[0] is None or num > threeLargest[0]:
		shiftAndUpdate(threeLargest, num, 0) # smallest number

# because we're not using a deque, we should define a shift method ourselves
def shiftAndUpdate(array, num, idx): # inputs: array, num to insert, index we want to shift buy
	for i in range(idx + 1): # goes from 0 to idx
		if i == idx: # if you find the index you were told to assign, 
			#assign it to the number you were told to use
			array[i] = num
		else: # assign that number to the next index, this will also rotate an array by as much as needed
			array[i] = array[i + 1] 
# EX: [x, y, z] and z is the num to update idx 2 (z) by -> [y, z, num] 
# EX: for index 1 (the middle index): it will go do i = 0 and 1, so it will first assign i'th val in the array
#to the old/current middle value, and then update the new middle value, then it's finished. 
