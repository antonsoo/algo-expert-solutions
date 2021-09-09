def removeDuplicatesFromLinkedList(linkedList):
	# O(n) time, O(1) space
	head = linkedList # our current node
    while head:
		nextUniquenode = head.next
		while nextUniquenode and head.value == nextUniquenode.value:
			# if the nextUniquenode.value is same as our current value
			# then the node over by one until you hit an actual unique/distinct node
			nextUniquenode = nextUniquenode.next
		# after we've found that nextUniquenode, head.next will equal to that
		# and then we just repeat the process again from our next node (the next Unique node)
		head.next = nextUniquenode
		head = nextUniquenode 
	return linkedList
