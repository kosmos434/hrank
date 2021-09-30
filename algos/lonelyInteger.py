# 🔢
#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

a = [1, 2, 3, 4, 3, 2, 1]


def lonelyinteger(a):
    num = [x for x in a if a.count(x) == 1][0]
    return(num)


lonelyinteger(a)
