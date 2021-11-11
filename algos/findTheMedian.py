#
import math
arr = [0, 1, 2, 4, 6, 5, 3]


def findMedian(arr):
    arr.sort()
    medianIndex = math.floor(len(arr)/2)
    return(arr[medianIndex])


findMedian(arr)
