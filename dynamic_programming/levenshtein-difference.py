"""
- problem: write a function that calculates the Levenshtein Distance
i.e., the minimum number of edits (deletions, replacements, insertions) to turn the first string into the second string
- solution: make a 2D matrix of the values of number of edits we have to do when converting str1 into str2.
- complexity: O(nm) time, O(nm) space.
"""
def levenshteinDistance(str1, str2):
    # define the 2D array:  (0th indeces will be the empty string so add + 1)
	n, m = len(str1), len(str2)
	# notice that the columns are already initialized, so we only initialize rows later
	numEdits = [[col for col in range(n + 1)] for row in range(m + 1)]
	# initialize the 2D array rows in the first column, in each row, it adds the prev element's number + 1
	for row in range(1, m + 1):
		numEdits[row][0] = numEdits[row - 1][0] + 1
	for row in range(1, m + 1):
		for col in range(1, n + 1):
			# we want to compare it at an offset so do - 1
			if str2[row - 1] == str1[col - 1]:
				# so if they match, just copy the value from the diagonal, since we don't need to do an edit. the num of edits is the same
				numEdits[row][col] = numEdits[row - 1][col - 1]
			else:
				# the formula is 1 more edit + the minimum between the previous diagonal, up, left values 
				numEdits[row][col] = 1 + min(numEdits[row - 1][col - 1], numEdits[row][col - 1], numEdits[row - 1][col])
	return numEdits[-1][-1] # return the very last edit count
