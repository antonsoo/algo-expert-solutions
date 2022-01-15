# O(n) time, O(1) space
def moveElementToEnd(array, toMove):
    p1 = 0
	p2 = len(array) - 1
	while p1 < p2: # exit when they meet or pass in the middle
		# already in a good place:
		if array[p2] == toMove: 
			# can also make this into a while loop: i<j and array[p2] == toMove: p2 -=1
			p2 -= 1
			continue
		# number at p1 is the right number:
		elif array[p1] == toMove:
			swap(p1, p2, array)
			p1 += 1
			#p2 -= 1 #unnecessary since above line does it
		# numbers at p1 and p2 are both wrong, keep p2, change p1
		else:
			p1 += 1
	return array
	

def swap(p1, p2, array):
	array[p1], array[p2] = array[p2], array[p1]
	#return array # not needed
