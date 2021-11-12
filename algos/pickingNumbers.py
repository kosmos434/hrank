# 🔢

import math
a = [4, 6, 5, 3, 3, 1]


def pickingNumbers(a):
    a.sort()
    final = 0
    for i in range(len(a)):
        oneOffNumbers = 1
        for j in range(i+1, len(a)):
            if abs(a[i] - a[j]) <= 1:
                oneOffNumbers += 1

        if oneOffNumbers > final:
            final = oneOffNumbers

    return(final)


pickingNumbers(a)
