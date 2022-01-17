# O(n) time, O(n) space
def firstDuplicateValue(array):
    d = {}
	for val in array:
		if val not in d: # seeing it for the first time
			d[val] = 1
		else: # seen it more than once
			return val
	return -1

# O(n) time and O(1) space
# do index=abs(val)-1 to find the index, -1 because array indeces start at 0.
# the number at this index will tell you if you've seen a val like that before.
# if you haven't seen it already, then turn the number at that index into a negative number.
# we can do this because the input is pos integers (between 1 and n)
def firstDuplicateValue(array):
	for val in array: # go through vals in the array
		index = abs(val) - 1
		if array[index] < 0: # negative
			return abs(val)
		else:  # positive
			# make it into a negative value that's already present there
			array[index] *= -1
	return -1 # nothing found
