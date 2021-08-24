def classPhotos(redShirtHeights, blueShirtHeights):
	# O(nlogn) time, O(1) space (technically O(n) space for the sort algo itself)
    redShirtHeights.sort()
    blueShirtHeights.sort()
    if redShirtHeights[0] > blueShirtHeights[0]:
      return compare(redShirtHeights, blueShirtHeights)
    elif redShirtHeights[0] < blueShirtHeights[0]:
      return compare(blueShirtHeights, redShirtHeights)
    else: 
      return False	

def compare(bigger, smaller):
  for i in range(len(bigger)): # lists have the same len
    if bigger[i] <= smaller[i]:
      return False
  return True
