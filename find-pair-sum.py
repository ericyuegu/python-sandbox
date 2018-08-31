# Given a sorted array of n distinct integers a1 < a2 < . . . < an and an integer X,
# you want to find if there exist indices i and j (where i != j) such that ai + aj = X.
# Give an O(n) comparison algorithm for this task.

'''
Returns:
	(i, j) if ai + aj = X
	None otherwise
'''
def findPair(arr, X):
	lower = 0
	upper = len(arr) - 1

	while lower < upper:
		if sum(arr[lower], arr[upper], X) == 0:
			return (lower, upper)
		elif sum(arr[lower], arr[upper], X) < 0:
			lower += 1
		else:
			upper -= 1

	return None

'''
Compute if the sum of pair (ai, aj) equals X

Returns:
	(i, j) if ai + aj = X
	None otherwise
'''
def sum(ai, aj, X):
	if (ai + aj) == X:
		return 0
	elif (ai + aj) < X:
		return -1
	else:
		return 1


def test():
	testArr = [-2, -1, 0, 3, 7, 11, 30, 49, 111]
	testX = 14
	print("Indices of pair of elements that add to " + str(testX) + " are " + str(findPair(testArr, testX)))

test()