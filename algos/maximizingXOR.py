# 📈

#
# Complete the 'maximizingXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

l = 10
r = 15


def maximizingXor(l, r):
    maxXOR = 0
    for i in range(l, r+1):
        for j in range(i+1, r+1):
            if i ^ j > maxXOR:
                maxXOR = i ^ j
    return(maxXOR)


maximizingXor(l, r)
