# problem: return the index of first non-repeating char in a string
#O(n) time, O(c<=26)->O(1) space 
def firstNonRepeatingCharacter(string):
	sdict = {} # a dictionary of letter:ind pairs, 
	#if the letter is seen more than once, ind is set to -1 because we dont care about it
	# count up all the occurences of each char in the string
	for ind, c in enumerate(string):
		if c in sdict:
			sdict[c] = -1
		else:
			sdict[c] = ind
	# go through our dict and find the first char that is only seen once
	for key, val in sdict.items():
		if val != -1:
			return val
	# if the condition above is never true
    return -1
