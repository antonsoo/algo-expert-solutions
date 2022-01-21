# This function will find the next node in a BST that's right after the target node, when going through the tree in an in-order traversal fashion.

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


# perform in-order traversal (O(n) time?) up to the next in-order node of the input node
# store in O(n) space
def findSuccessor(tree, node):
    inOrderResult = inOrder(tree) # O(n) space 
	# now traverse the in-order traversal organized array, we want to find the next in-order node
	for idx, currentNode in enumerate(inOrderResult):
		if currentNode != node: # skip the node we're not looking for
			continue 
		#else
		# if we ran over the number of elements:
		if idx == len(inOrderResult) - 1:
			return None
		# else
		# we found our node so now lets return the next node after it (from our in-order traversal)
		return inOrderResult[idx + 1]
	

def inOrder(node, result=[]): # in order traversal, returns the order in 'result'
	if node is None:
		return result
	# else:
	inOrder(node.left, result)
	result.append(node)
	inOrder(node.right, result)
	return result
