# can start from any index
# run/iterate the loop with len(array) number of times
# it should end up at the original array index at the end
# return true if so, and false if not
# brute force, just try what the array says: O(n) time, O(1) space

def hasSingleCycle(array):
    leng = len(array)
	if leng <= 1:
		return true
	# lets just start with the 0 index, might work for all others if this works
	index = 0
	counter = 0
	while counter < leng:
		if counter > 0 and index == 0: # can't go anywhere if zero steps to jump
			return False
		index = (index + array[index]) % leng # set the new value
		if index < 0:
			index = index + leng
		counter += 1
	#last_index = (index + array[index])%leng # set the new value
	return index == 0#last_index == 0 and index != 0 

# index = 1, counter = 2
