# Given a sorted array of n distinct integers a1 < a2 < . . . < an,
# you want to find if there is an index i such that ai = i.
# Give an O(log n) comparison algorithm for this task.

def findFixedPoint(array, lower, upper):
    if upper >= lower:
        mid = (lower+ upper) // 2
    else:
        return None

    if mid == array[mid]:
        return mid

    if mid > array[mid]:
        return findFixedPoint(array, (mid + 1), upper)
    else:
        return findFixedPoint(array, lower, (mid - 1))

    return None

def test():
    testArray = [-2, -1, 0, 3, 7, 11, 30, 49, 111]
    n = len(testArray)
    print("Fixed point is: " + str(findFixedPoint(testArray, 0, n - 1)))

test()
