# problem: iterate through an n x m array in a spiral manner
# O(n) time to iterate through the array, O(n) space for the output
def spiralTraverse(array):
    output = [] # result
	n, m = len(array), len(array[0])
	startrow, startcol = 0, 0
	endrow, endcol = n - 1, m - 1
	
	# iterate through the outer perimeter in a spiral manner until, then move the perimeter inwards
	while startrow <= endrow and startcol <= endcol:
		# iterate through the upper perimeter, rightwards:
		for col in range(startcol, endcol + 1):  # +1 because our endcol is len(n) - 1, and range ends before it gets there
			output.append(array[startrow][col])
		# iterate through the right perimeter, downwards:
		for row in range(startrow + 1, endrow + 1): # +1 to startrow so we don't double count it
			output.append(array[row][endcol])
		# iterate backwards through the bottom perimeter, leftwards:
		for col in reversed(range(startcol, endcol)): # notice no +1 this time
			if startrow == endrow: # edge case, when a single row is left in the middle, don't double count it
				break
			output.append(array[endrow][col])
		# iterate backwards through the right perimeter, upwards:
		for row in reversed(range(startrow + 1, endrow)): # notice no +1 this time on endrow, but instead on startrow
			if startcol == endcol:  # edge case, when a single column is left in the middle, don't double count it
				break
			output.append(array[row][startcol])
		# update the bounds; move them inwards:
		startrow += 1
		startcol += 1
		endrow -= 1
		endcol -= 1
	return output

######################################################################################

# recursive solution: almost identical to the original one
# O(n) time to iterate through the array, O(n) space for the output
# extra space is used for the recursive callstack compared to the iterative solution
def spiralTraverse(array):
	output = [] # result
	n, m = len(array), len(array[0])
	startrow, startcol = 0, 0
	endrow, endcol = n - 1, m - 1
	spiralrecursive(output, startrow, endrow, startcol, endcol, array)
	return output

# iterate through the outer perimeter in a spiral manner until, then move the perimeter inwards
def spiralrecursive(output, startrow, endrow, startcol, endcol, array):
	# base case:
	if startrow > endrow or startcol > endcol:
		return
	
	# iterate through the upper perimeter, rightwards:
	for col in range(startcol, endcol + 1):  # +1 because our endcol is len(n) - 1, and range ends before it gets there
		output.append(array[startrow][col])
	# iterate through the right perimeter, downwards:
	for row in range(startrow + 1, endrow + 1): # +1 to startrow so we don't double count it
		output.append(array[row][endcol])
	# iterate backwards through the bottom perimeter, leftwards:
	for col in reversed(range(startcol, endcol)): # notice no +1 this time
		if startrow == endrow: # edge case, when a single row is left in the middle, don't double count it
			break
		output.append(array[endrow][col])
	# iterate backwards through the right perimeter, upwards:
	for row in reversed(range(startrow + 1, endrow)): # notice no +1 this time on endrow, but instead on startrow
		if startcol == endcol:  # edge case, when a single column is left in the middle, don't double count it
			break
		output.append(array[row][startcol])
		
	# update the bounds; move them inwards, calling the function identically:
	spiralrecursive(output, startrow + 1, endrow - 1, startcol + 1, endcol - 1, array)
