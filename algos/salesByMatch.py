# 🧦


import math
ar = [1, 2, 1, 2, 1, 3, 2]
n = len(ar)


def sockMerchant(n, ar):
    pairCount = 0
    uniquesInAr = list(set(ar))
    for i in uniquesInAr:
        pairCount += math.floor(ar.count(i) / 2)

    return(pairCount)


sockMerchant(n, ar)
