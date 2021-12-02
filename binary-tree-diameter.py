# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) time, O(h) space
class TreeInfo:
	def __init__(self, diameter, height): # our own class, height is unnecessary but it's good practice
		self.diameter = diameter
		self.height = height

def helper(tree):
	# base case
	if not tree: # is None
		return TreeInfo(0, 0) # an object with (0, 0) height and diam
	
	# call recursively
	leftInfo = helper(tree.left)
	rightInfo = helper(tree.right)
	
	# calculate info
	longestPath = leftInfo.height + rightInfo.height # longest path through root
	maxDiam = max(leftInfo.diameter, rightInfo.diameter) # max diameter so far
	currentDiam = max(longestPath, maxDiam)
	
	# you don't need to calculate height for this answer but why not0
	currentHeight = 1 + max(leftInfo.height, rightInfo.height) #  adds max height and 1 each time the func is called recursively
	
	# return an object with the current/max diam and current/max height
	return TreeInfo(currentDiam, currentHeight)
	
def binaryTreeDiameter(tree):
    return helper(tree).diameter # returns the instance variable from the object created in the helper function

  
  ################# second way:
  def binaryTreeDiameter2(tree):
    diameter = 0

    def longest_path(node):
      if not node:
        return 0
      nonlocal diameter
      # recursively find the longest path in
      # both left child and right child
      left_path = longest_path(node.left)
      right_path = longest_path(node.right)

      # update the diameter if left_path plus right_path is larger
      diameter = max(diameter, left_path + right_path)

      # return the longest one between left_path and right_path;
      # remember to add 1 for the path connecting the node and its parent
      return max(left_path, right_path) + 1

    longest_path(tree)
    return diameter
  
