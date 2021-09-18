# ⭕

from collections import deque
a = [3, 4, 5]
k = 2
queries = [1]


def circularArrayRotation(a, k, queries):
    a = deque(a)
    a.rotate(k)
    a = list(a)
    print(a)

    returnList = []
    for i in (queries):
        returnList.append(a[i])
    return(returnList)


circularArrayRotation(a, k, queries)
