# =

arr = [1, 2, 2, 3]


def equalizeArray(arr):
    maxx = 0
    maxxnum = 0
    deletions = 0
    for i in arr:
        thisCount = arr.count(i)
        if thisCount > maxx:
            maxx = thisCount
            maxxnum = i

    for i in arr:
        if i != maxxnum:
            deletions += 1

    return(deletions)


equalizeArray(arr)
