# O(n) time, O(1) space
def isMonotonic(array):
	if len(array) < 2:
		return True
	lastnum = array[0]
	# checking my number against the last number in the array will tell me if the whole thing is increasing or not
	if array[-1] >= lastnum: # increasing or equal
    	for num in array[1:]:
			if num >= lastnum:
				lastnum = num
				continue
			else:
				return False
		return True
	elif array[-1] <= lastnum: # decreasing or equal
		for num in array[1:]:
			if num <= lastnum:
				lastnum = num
				continue
			else:
				return False
		return True
