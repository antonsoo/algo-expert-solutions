# O(n) time, O(n) space
def firstDuplicateValue(array):
    d = {}
	for val in array:
		if val not in d: # seeing it for the first time
			d[val] = 1
		else: # seen it more than once
			return val
	return -1
