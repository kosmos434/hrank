# 🌳


#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

n = 5


def utopianTree(n):
    height = 0
    spring = False
    for i in range(n+1):
        if spring:
            height = height * 2
            spring = not spring
        else:
            height = height + 1
            spring = not spring
    return(height)


utopianTree(n)
