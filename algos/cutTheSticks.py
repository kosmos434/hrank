# 🏒

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

arr = [1, 2, 3, 4, 3, 3, 2, 1]


def cutTheSticks(arr):
    lengths = []

    while len(arr) > 0:
        lengths.append(len(arr))
        arr = [x for x in arr if x != min(arr)]
    return(lengths)


cutTheSticks(arr)
