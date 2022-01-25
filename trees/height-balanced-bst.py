# problem: return true if the input tree is balanced by height

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# we will make an extra class so that the code looks cleaner
class TreeInfo:
	def __init__(self, balanced, height):
		self.balanced = balanced # boolean value
		self.height = height # int
	
# O(n) time, O(h) space  (n is the number of nodes, h is the height)
def heightBalancedBinaryTree(tree):
	# use the class and function we've defined to go through the tree  
	treeInfo = getTreeInfo(tree) # this returns and assigns treeInfo to the TreeInfo class returned from the function we used
	return treeInfo.balanced # boolean value ran on the root value will tell us if the overall tree is balanced or not
	
# calculates if the tree is balanced on a node, recursively
def getTreeInfo(node):
	# base case:
	if node is None: # went to a node that doesn't exist after an ending of another node
		return TreeInfo(True, -1) # True by default, -1 height
	# recursively repeat:
	leftsubtree = getTreeInfo(node.left)
	rightsubtree = getTreeInfo(node.right)
	
	balanced = (leftsubtree.balanced and rightsubtree.balanced  # True and True boolean
				  and abs(leftsubtree.height - rightsubtree.height) <= 1) # heights are good (less than 1 diff)
	height = max(leftsubtree.height, rightsubtree.height) + 1 # calculate/update the current height
	return TreeInfo(balanced, height) # return the info object of the current tree
	
	
