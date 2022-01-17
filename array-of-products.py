# O(n) time ? and O(n) space
from math import prod
def arrayOfProducts(array):
    prods = [prod(array[1:])] # with initial value
	for ind in range(1, len(array) - 1):
		prods.append(prod(array[0:ind]) * prod(array[ind+1:]))
	prods.append(prod(array[:-1])) # last num
	return prods
