# O(n) time and O(d) space, because your call stack will maximally be the deepest size/depth of your tree
def validateBst(tree):
	return helper(tree, float('-inf'), float('inf'))

def helper(tree, minv, maxv):
	if not tree: # if it's None then return True by default, and go back up the call stack
		return True
	if tree.value < minv or tree.value >= maxv:
		return False
	left = helper(tree.left, minv, tree.value) # left value must be between -inf and its root: -inf<left<root.val
	right = helper(tree.right, tree.value, maxv) # right value must be between root val and inf: root.val<right<inf
	return left and right # returns true if both conditions are met
