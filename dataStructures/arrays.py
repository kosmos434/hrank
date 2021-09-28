# ☀☀

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

a = [1, 4, 3, 2]


def reverseArray(a):
    newArr = []
    for i in range(len(a) - 1, -1, -1):
        newArr.append(a[i])
    return newArr


reverseArray(a)
