"""
"array": [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
you have to find length of the longest peak and output that length
in this case it's 6, the subarray [0, 10, 6, 5, -1, -3]
"""

# official code from my memory
# ~O(N) time, O(1) space 
def longestPeak(array):
    longestPeakLength = 0
	i = 1 # start with index 1 
	while i < len(array) - 1: # dont iterate over the last ind in the array
		# find a peak, store it as a boolean value if it meets the conditions:
		isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]
		if not isPeak: # if it didnt meet the condition:
			i += 1 # increment the index (move on)
			continue # dont run the rest of the loop, move on from the top
		
		#else: # we found the peak, now lets calculate its length
			# check the bounds and if it meets the condition, while it keeps doing that, increment the length	
		leftIdx = i - 2 # continue from the left slope being to the right of array[i-1] since we know that's already our peak's left
		while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
			leftIdx -= 1

		rightIdx = i + 2 # continue from array[i+1] since we know that's already good
		while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:	
			rightIdx += 1

		currentPeakLength = rightIdx - leftIdx - 1 # this will work even if the left i - 2 or right i + 2 is out of bounds :)
		longestPeakLength = max(currentPeakLength, longestPeakLength)
		i = rightIdx # reset the index to be the index right after our peak ends
			
	return longestPeakLength




"""
 my unfinished solution:
the way the official solution does it is: 
 they find a peak, and then go left and right to see if the left of the peak keeps decreasing, and the right keeps decreasing the other way, and thus they know the length of this peak
 I calculate to see the actual change in the array and keep track of the change as a flag variable, if the change happens twice, I stop the loop and reset my currentpeaklength variable back to zero
I believe my solution is O(N), while the official solution is also supposedly O(N), I think it is technically like O(N/2 + N)
"""
# O(n) time, O(1) space.
def longestPeak(array):
	globalmax = 0
	currentmax = 0
	changed = 0 # to keep track for the pattern/sign of the slope changing twice so we stop counting
    # problem: my code only checks if the slope drops off right after increasing
	#I also need to do the same thing for when it keeps decreasing
	for ind in range(1, len(array)):
		prev = array[ind - 1]
		curr = array[ind]
		if prev < curr: # the pattern continues, it keeps increasing
			currentmax += 1
			# we will do it here as well in case the array is short and ends quickly or not a lot of changes in it
			if currentmax > globalmax:
				globalmax = currentmax
			
		else: # check if the pattern/slope changed twice
			if changed < 1:
				changed += 1
				if prev < curr: # the pattern continues, it keeps increasing
					current max += 1
			else: # count the current largest change and reset it
				currentmax += 1
				if currentmax > globalmax:
					globalmax = currentmax
				currentmax = 0
	return globalmax
