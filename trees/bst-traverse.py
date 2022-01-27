# For all funcs: O(n) time to go through each node, O(n) space for the array. 

def inOrderTraverse(tree, array):
	# base case for recursion:
	if tree is None: # tree is a node input 
		return  # if the node is None, then return nothing and go back
    inOrderTraverse(tree.left, array)
	array.append(tree.value) # in the case we've reached an actual node
	inOrderTraverse(tree.right, array)
	return array

def preOrderTraverse(tree, array):
	# base case for recursion:
	if tree is None: # tree is a node input 
		return  # if the node is None, then return nothing and go back
	array.append(tree.value)  # in the case we've reached an actual node
	preOrderTraverse(tree.left, array)
	preOrderTraverse(tree.right, array)
	return array

def postOrderTraverse(tree, array):
	# base case for recursion:
	if tree is None: # tree is a node input 
		return  # if the node is None, then return nothing and go back
	postOrderTraverse(tree.left, array)
	postOrderTraverse(tree.right, array)
	array.append(tree.value)  # in the case we've reached an actual node
	return array
