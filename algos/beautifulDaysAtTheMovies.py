# 🍿📽

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

i = 20
j = 23
k = 6


def beautifulDays(i, j, k):
    bdays = 0
    for x in range(i, j+1):
        reverse = int(str(x)[::-1])
        beautiful = abs(x-reverse)
        if beautiful % k == 0:
            bdays += 1
    return(bdays)


beautifulDays(i, j, k)
