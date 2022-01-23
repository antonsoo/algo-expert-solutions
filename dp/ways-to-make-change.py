# input: n is amount we're trying to make, 'denom' demons of the money given
# output, the number of ways we can make the change in the amount n, from denoms
# O(n*d) time, O(n) space
def numberOfWaysToMakeChange(n, denoms):
	if len(denoms) < 1: # basic fail case, zero ways to make the change
		return 0
	# the indeces in ways aray correspond to amounts we can make. So all amounts from 0 amount of money to n+1
	# and the actual values are the number of ways we could make that amount  
    ways = [0 for amount in range(n + 1)] # numbers of ways to make change 
	# this question assumes it's possible to make at the amount from at least one of the denoms
	ways[0] = 1 # start the number of ways to be 1
	# go through each denom
	for d in denoms:
		# go through each amount for each denom
		for amount in range(1, n + 1):
			if d <= amount: 
				# add to the current num of ways what we have so far
				# number of ways to make that amount so far  + numbers of ways to make that amount from that coin
				ways[amount] = ways[amount] + ways[amount - d]
				# Ex: ways[10] = ways[10] + ways[10 - 5] = ways[10] + ways[5] = 2 + 2 = 4
	return ways[-1] # if it doesn't change, like from o
