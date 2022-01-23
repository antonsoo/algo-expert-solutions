# problem: try to see if you can generate a sentence/document from the given characters/sentence
# make a dict or a defaultdict that stores the letters, if there are >= num of letters in the dict for that letter,
# then we can generate the text.
# O(n) + O(m) time to go through each array -> O(n) time. O(c) space for the number of unique chars to store in the dict
# we could count up the number of type of chars and compare them after, but that's extra time and memory.
#instead we can just take away from the chars dict, if there is nothing, we return False right away
def generateDocument(characters, document):
	chars = {}
	for c in characters:
		if c in chars: # if it already exists, update the count for that char
			chars[c] += 1
		else: # else write it down
			chars[c] = 1
	for c in document:
		if c in chars:
			chars[c] -= 1
			if chars[c] == 0: # if it reaches 0, remove it
				del(chars[c])
		else: 
			return False # can also put this at the top and remove the else
	return True # if it passes the above test, it moves on
