# 🟧

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

import math
a = 3
b = 9


def squares(a, b):
    # DUMB BRUTE FORCE WAY
    # squaresCount = 0
    # for i in range(a, b+1):
    #     lastDigit = i % 10
    #     if lastDigit in [2, 3, 7, 8]:
    #         continue
    #         # print(i, " square rooted = ", math.sqrt(i))
    #         # print(float(i))
    #     rooted = math.sqrt(i)
    #     if ((rooted % 1) == 0):
    #         i = int(rooted) + 1
    #         squaresCount += 1
    # return(squaresCount)

    # a range of possible roots in the og range
    # like 9-25 will have a rooted range of 3-5, or 3 perf. squares
    start = math.sqrt(a)
    end = math.sqrt(b)
    # print(start, end)
    return(math.floor(end) - math.ceil(start) + 1)


squares(a, b)
