 
 # O(n) time, space 
def twoNumberSum(array, targetSum): # assuming no edge cases
  mem = {}
	for num in array:
		diff = targetSum - num
		if diff in mem:
			return [diff, num]
		else:
			mem[num] = 7 # can assign any value here
	return [] # no possible answer
		
 # O(n) time, space 
def twoNumberSum(array, targetSum): 
	if len(array) < 2: # edge case
		return []
    mem = [] # can also do mem = {}
	for ind, num in enumerate(array):
		diff = targetSum - num # this will be the number we're trying to find, if we're already seen it
		if diff in mem:
			return [diff, num]
		#else:
		mem.append(num) # for a dict: mem[num] = 0 # add it to the dict. the val doesnt matter
	return [] # if it never finds our value  
