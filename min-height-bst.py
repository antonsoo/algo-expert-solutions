class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

# assume all integers in the array are unique (!), and sorted.
# O(nlogn) time because inserting into a BST tree, O(N) space
def minHeightBst1(array):
    return constructMinHeightBst(array, None, 0, len(array) - 1)
def constructMinHeightBst(array, bst, startIdx, endIdx):
	if endIdx < startIdx:
		return
	midIdx = (startIdx + endIdx) // 2
	valueToAdd = array[midIdx]
	if bst is None: # if there is no BST being used already... (first iteration)
		# to make a BST, you need a value
		bst = BST(valueToAdd)
	else:
		bst.insert(valueToAdd)
	constructMinHeightBst(array, bst, startIdx, midIdx - 1)
	constructMinHeightBst(array, bst, midIdx + 1, endIdx)
	return bst
  
  
# O(N) time, O(N) space. Same as the other one, just neater code.
# instead of manually adding the trees in our code, just call the function recursively in the assignment
def minHeightBst2(array):
   return constructMinHeightBst(array, 0, len(array) - 1)
def constructMinHeightBst3(array, startIdx, endIdx):
	if endIdx < startIdx:
		return None
	midIdx = (startIdx + endIdx) // 2
	bst = BST(array[midIdx])
	bst.left = constructMinHeightBst(array, startIdx, midIdx - 1)
	bst.right = constructMinHeightBst(array, midIdx + 1, endIdx)
	return bst
  
