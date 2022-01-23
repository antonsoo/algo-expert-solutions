# This is an input class. Do not edit.
class Node:
	# example DLL: None<-node0,val0(head)<->node1,val1<->node2,val2<->node3,val3(tail)->None
    def __init__(self, value):
        self.value = value
		# doubly-linked list, at minimum None<-Head/Tail->None 
        self.prev = None
        self.next = None

# DLL can be used in things like web browsers that have backwards and forwards function between page 
#or any time you have to go backwards and forwards quickly
# LL are fast to remove and access an item, but may take time to find it
# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

	# O(1) time and space	
    def setHead(self, node): #7th func
		# if the tail and head are None; it was an empty LL
		if self.head is None:
			self.head = node
			self.tail = node
			return
		# else
		# update it. The function actually already takes care of the case in which it might be a head as input
		self.insertBefore(self.head, node)
	
	# O(1) time and space
    def setTail(self, node): #8th func
        if self.tail is None:
			#self.head = node
			#self.tail = node
			self.setHead(node) # same as above since it's done in that function
			return
		# else, insert after the current tail, and that will become a new tail as defined in our function
		self.insertAfter(self.tail, node)
		
	# O(1) time and space
	# insert node 'nodeToInsert' before node 'node'
    def insertBefore(self, node, nodeToInsert): #5th func
		# if the nodeToInsert is both the head and the tail, don't do anything
        if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		self.remove(nodeToInsert) # we should remove the node if it's already in our linked list (the literal node, not a node with that value!)
		# Ex: insert before 2: N<-1<->2->None  -becomes>  N <- 1 <-> NewNode <-> 2 -> None 
		# write bindings for nodeToInsert
		nodeToInsert.prev = node.prev # the new node's back should be the current node's back connection
		nodeToInsert.next = node # the new node's next pointer is just pointing to the current node since it's behind the current node
		# now update the bindings of the surrounding nodes; rewrite bindings for the neighboring nodes of our new node
		if node.prev is None: # if we're inserting before the Head, update the head
			self.head = nodeToInsert
		else: # the prev node is not the head
			# update the next pointer of the previous node that was behind the node (node.prev)
			node.prev.next = nodeToInsert
		node.prev = nodeToInsert # set the backwards pointer of the current node to the new backwards node
	
	# O(1) time and space
    def insertAfter(self, node, nodeToInsert): #6th func
        # edge case:
		if nodeToInsert == self.head and nodeToInsert == self.tail:
			return # don't do anything
		self.remove(nodeToInsert) # if it's already there
		# write bindings for nodeToInsert
		nodeToInsert.prev = node
		nodeToInsert.next = node.next
		# rewrite bindings for the neighboring nodes of our new node
		if node.next is None: # if it's the tail
			self.tail = nodeToInsert # the new tail is this
		else:
			node.next.prev = nodeToInsert
		node.next = nodeToInsert # update the forward pointer of the current node

	# O(p) time, O(1) space
    def insertAtPosition(self, position, nodeToInsert): # last function to write
        if position == 1: # we're at the head so do the function we wrote previously, remember pos 0 is the None that self.head points to
			self.setHead(nodeToInsert) 
			return
		# else, go through the array until we find our position or we never find it/error:
		node = self.head
		currentPosition = 1
		while node is not None and currentPosition != position:
			node = node.next
			currentPosition += 1
		# if the next node is not None (node=node.next in the prev line of code, look)
		if node is not None: # insert before the current node because it will become the new position
			self.insertBefore(node, nodeToInsert)
		else: # the next node is None so we have to make nodeToInsert the new tail
			self.setTail(nodeToInsert)
		
    def removeNodesWithValue(self, value): #4th function
        # traverse the list like before
		node = self.head
		while node is not None:
			nodeToRemove = node # temporary variable because we'll reassign it 
			node = node.next
			if nodeToRemove.value == value:
				self.remove(nodeToRemove)
				
	# O(1) time and space
    def remove(self, node): # 2nd function
		# this will make sure this edge case works: None <-- Head&Tail --> None
        # in the case we're removing the head of the DLL:
		if node == self.head:
			self.head = self.head.next # move the head over by one node
		# in the case we're removing the tail of the DLL:
		if node == self.tail:
			self.tail = self.tail.prev
		self.removeNodeBindings(node) # updates the pointers/bindings of a node for removal

		# this search function can be improved upon, like starting from the start and end and convering the two pointers 
		#that is O(N/2) but it's still ~O(N) time. Maybe it can be improved even further. Especially if the LL is known to be sorted!
		# This function is O(N) time. O(1) space.
    def containsNodeWithValue(self, value): # 1st function to implement
        node = self.head # stat at the beginning of our DLL
		# traverse through the DLL, unless we hit the start/end or if we find the value
		while node is not None and node.value != value:
			node = node.next
		# this will return True only if the node is not None, so only if we found our node in the while loop above
        return node is not None # boolean statement
	
	# a custom function for removing node bindings
	def removeNodeBindings(self, node): # 3rd function to implement
		# overwrite node.prev if it exists:
		if node.prev is not None:
			node.prev.next = node.next
		# do the same thing with node.next if it exists
		if node.next is not None:
			node.next.prev = node.prev
		# we have to do both of these at the end after the prev stuff (before we rewrite them.) unless we use temp variables
		node.prev = None # now overwrite it to None
		node.next = None
