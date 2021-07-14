def nonConstructibleChange(coins):
	# O(nlogn) time, O(n) space (both are because of sorting)
	highest_change = 0
	for coin in sorted(coins):
		if coin > highest_change + 1:
			return highest_change + 1
		else:
			highest_change += coin
    return highest_change + 1
