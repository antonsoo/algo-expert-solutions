def smallestDifference(arrayOne, arrayTwo):
    # O(nlogn + mlogm) time, O(1) space
	# sort in place and then look using two pointers, incrementing intelligently 
	# assuming: the lens of arrays can be different, they're unsorted as input, the input is always\
	#*an integer array* (of any size, neg/pos). And input size is at least 1. 
	
	arrayOne.sort()
	arrayTwo.sort()
	
	L1 = len(arrayOne)
	L2 = len(arrayTwo)
	# indices:
	i, j = 0, 0
	minim = float('inf')
	ans = [arrayOne[i], arrayTwo[j]] # initialize output array
	while i < L1 and j < L2:
		num1, num2 = arrayOne[i], arrayTwo[j]
		if num1 == num2:
			return [arrayOne[i], arrayTwo[j]]
		# bigger num minus smaller num
		# if the diff is smaller than the current minim
		# move the pointer of the smaller num to make it bigger 
		elif num1 < num2: 
			diff = num2 - num1
			i += 1
		else: #num1 > arrayTwo[j] 
			diff = num1 - num2
			j += 1
		if diff < minim: # not sure why we dont need abs(diff)
			minim = diff
			ans = [num1, num2]
	return ans
