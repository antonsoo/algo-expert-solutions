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


#---------------------------------second solution
# O(nm) time, O(min(n,m)) space
def levenshteinDistance(str1, str2):
	n, m = len(str1), len(str2)
	# assign the smallest and biggest strings
	if n < m:
		small, big = str1, str2
	else:
		small, big = str2, str1
	smalln, bign = len(small), len(big)
	evenEdits = [x for x in range(smalln + 1)]
	oddEdits = [None for x in range(smalln + 1)] # can replace None with anything
	for i in range(1, bign + 1):
		if i % 2 == 1: # odd
			currentEdits = oddEdits
			previousEdits = evenEdits
		else: # even
			currentEdits = evenEdits
			previousEdits = oddEdits
		currentEdits[0] = i
		for j in range(1, smalln + 1):
			if big[i - 1] == small[j - 1]:  # if the equal, make it current equal the previous value so no change
				currentEdits[j] = previousEdits[j - 1]
			else: # use the formula as before, taking min between the prev diag, up, and left values
				currentEdits[j] = 1 + min(previousEdits[j - 1], previousEdits[j], currentEdits[j - 1])
	return evenEdits[-1] if len(big) % 2 == 0 else oddEdits[-1] # return evenEdits if even, or else


#---------------------------------------------my failed attempt:
def levenshteinDistance(str1, str2):
	i, j = 0, 0
	n, m = len(str1), len(str2)
	wordSimilarityScore = 0
	differenceScore = 0
	for c1idx in range(i, n):
		for c2idx in range(j, m):
			if str1[c1idx] == str2[c2idx]: # match
				wordSimilarityScore += 1
				i += 1
				j += 1
				break # break the current loop so the outer loop can restart with the new vars
		differenceScore += 1
	#return wordSimilarityScore
	return max(abs(differenceScore - wordSimilarityScore), wordSimilarityScore) 
