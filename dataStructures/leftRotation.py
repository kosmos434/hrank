# 👈

d = 4
arr = [1, 2, 3, 4, 5]


def rotateLeft(d, arr):
    returnArray = []
    for i in range(len(arr)):
        something = (i + d) % len(arr)
        returnArray.append(arr[something])

    return(returnArray)


rotateLeft(d, arr)
