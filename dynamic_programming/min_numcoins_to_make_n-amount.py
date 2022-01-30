"""
- problem: return the min number of coins from the given coin types (denoms) to get the target sum
- solution: reuse an array with values representing the min. number of coins to make that amount (the indeces)
so we use dynamic programming by reusing the precomputed num. of coins like a memory, instead of computing it over again
- complexity: O(n*d) time, O(n) space
"""

def minNumberOfCoinsForChange(n, denoms):
	# numcoins array has: indices representing the amounts we can make, (add 1 index so we dont start at 0 sum)
	#all the way to the amount we're trying to make, n, 
	#and the values represent the min. number of coins that it takes to make that amount
	numcoins = [float('inf') for _ in range(n + 1)] # initialize as very high because we want to replace it right away if possible to make an amount like that using our coins
	#base case:
	numcoins[0] = 0 # a zero amount is made with 0 coins
	# built up the numcoins array, by going through 
	for denom in denoms: # go through each coin type/denom
    	for amount in range(len(numcoins)): # go through n+1 amounts, incrementally
			if denom <= amount: # if we can at least attempt to make that amount with our current denom/coin
				# if it's not smaller, keep the number there, else, (the minimum out of the two is)
				#1 plus the amount that we would get from that amount-denom.
				numcoins[amount] = min(numcoins[amount], 1 + numcoins[amount - denom])  
				#Ex: 1+numcoins[4-2]=1+numcoins[2]= for the amount 4, using the coin 2, we could make it using the same coin, 2, plus another of the same coin, thus +1 
    # if we actually get to our amount, we will return the min number of coins we used to get it
	if numcoins[n] != float('inf'):
 		return numcoins[n]
	else: # if we never do, return -1
		return -1
