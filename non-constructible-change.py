def nonConstructibleChange(coins):
	highest_change = 0
	for coin in sorted(coins):
		if coin > highest_change + 1:
			return highest_change + 1
		else:
			highest_change += coin
    return highest_change + 1
