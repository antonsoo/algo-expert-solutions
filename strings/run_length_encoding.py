# problem: encode any chars by their num of occurences. split than if they're more than 9. like AAAABB -> 3A2B
# assume input is any standard char: letters/symbols/numbers/emptychar a string and it can be empty/only spaces
# O(N) time to go through each char, O(N) space for the output
def runLengthEncoding(string): 
	output = ""
    for char in string:
		if len(output) < 1: # just starting, so add the char to the string
			output += "1" + char
			continue # continue so you don't double count it 
		if output[-1] == char: # if it's already there, and we're seeing another one like this
			if int(output[-2]) < 9: # look at the number in front of this char if it's less than 9
				# modify that number, remember strings in Py are immutable, so we have to do this:
				output = output[:-2] + str(int(output[-2]) + 1) + output[-1] # increment and replace the char there
			else: # too full so make a new one and add it to the string
				output += "1" + char 
		else: # we're seeing it for the first time
			output += "1" + char
	return output 
