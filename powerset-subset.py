"""
Ex: start with [[]]  , input [1, 2, 3] 
combine [] with [1]: [], [1]
next: [], [1] combine with [2]: [],[1],[2],[1, 2]  (notice how we go one by one following the formula above)
next:  [],[1],[2],[1, 2] with [3], . .. 
"""
def powerset(nums):
	powersetOutput = [[]] # output. Already initialize the empty set (technically, array).
	for num in nums:
		powersetOutput += [(subset + [num]) for subset in powersetOutput]
	return powersetOutput






#-------------------------------unfinished solution:
"""
problem: return the powerset of an array. E.g., [1,2] -> [[], [1], [2], [1, 2], [2, 1]]

"""
def powerset(array):
	powerset = [[]] # output, start with the empty set/array
    n = len(array)
	for i in range(n):
		# count and append all combinations to the powerset array of arrays
		appendCombinations(array[i:n], powerset, 0)
	return powerset

def appendCombinations(array, powerset, 0):
	if len(array) <= 0 or i == 0:
		powerset

