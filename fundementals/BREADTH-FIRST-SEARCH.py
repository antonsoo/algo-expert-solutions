# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.

# The algorithm:
# take the current elem (parent) which is the first elem of the queue (pop the queue) 
# put it into your output array
# if it has children, put of all of parent's children into the queue
# repeat until the end

# The time complexity:
# worst: O(V+E) time, you compute all of the children nodes with children or no children by adding them to your output array
# and you compute all of the children (edges) for each node (your loop/recursive calls)
# worst: O(V) space, to hold V nodes/vertices for the queue (and for the output array if you're not given that)
from collections import deque # can also do: import collections, and collections.deque()
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
	
    def breadthFirstSearch(self, array): # array is the given empty searched through array using BFS
		# the input is done through the class, so it's "self", that's the root/main parent of the tree
		queue = deque([self]) # implementing a queue using a list, just use pop(0) to pop the first elem. self is the parent/first node BTW, initializing like collections.deque() also works but only with normal lists for some reason 
		while len(queue) > 0: # you actually iterate through a tree by accessing a/the root's children and going back up, when there are no children
			current = queue.popleft() # the front of the queue
			array.append(current.name)
			for child in current.children: #.children is a list attribute of the Node object you're iterating through
				queue.append(child)
		return array
  
  # list queue implementation solution. Unoptimal because if there are M children for a node, the queue will run M times. so N number of nodes * M total.  
  def breadthFirstSearch2(self, array):
		queue = [self]
		while len(queue) > 0:
			current = queue.pop(0)
			array.append(current.name)
			for child in current.children: 
				queue.append(child)
		return array
		
