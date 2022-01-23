# input: a string of lowercase chars with no spaces
# remember, each letter has a uniquecode associated with it, we can convert it to that + the key value, and wrap it around
# O(n) time, O(n) space
def caesarCipherEncryptor(string, key):
	newstr = ""
	key = newkey % 26 # in case the key value is too high
	for char in string:
		# convert to order and add the key
		tmp = ord(char) + newkey
		if tmp > 122: # 'z' is 122
			newstr += chr(96 + tmp % 122)
		else:
			newstr += chr(tmp)
	return newstr
	
# input: a string of lowercase chars with no spaces
# remember, each letter has a uniquecode associated with it, we can convert it to that + the key value, and wrap it around
# O(n) time, O(n) space
def caesarCipherEncryptor(string, key):
	newstr = ""
	for char in string:
		# convert to order and add the key
		tmp = ord(char) + key
		# this is not efficient if our key is extremely large
		while tmp > 122: # 'z' is 122
			tmp -= 26 
		newstr += chr(tmp)
	return newstr

# Doesn't use ord() or chr()
def caesarCipherEncryptor(string, key):
    newstr = ""
	newkey = key % 26
	alphabet = list("abcdefghijklmnopqrstuvwxyz")
	for c in string:
		newstr += getNewC(c, newkey, alphabet)
	return newstr
def getNewC(char, key, alphabet): # gets the new character/letter index
	newcharcode = alphabet.index(char) + key
	return alphabet[newcharcode % 26]
