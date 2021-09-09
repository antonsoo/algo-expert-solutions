def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
  # O(nlogn) time, O(1) space  (technically O(n) space for the sort itself)
  redShirtSpeeds.sort()
	total = 0
	if fastest:
		blueShirtSpeeds.sort(reverse=True)
		for i in range(len(redShirtSpeeds)): # assume their lengths are equal
			total += max(redShirtSpeeds[i], blueShirtSpeeds[i])
	else:
		blueShirtSpeeds.sort()
		for i in range(len(redShirtSpeeds)): # assume their lengths are equal
			total += max(redShirtSpeeds[i], blueShirtSpeeds[i])
	return total
