# 🏁

k = 7
height = [1, 6, 3, 5, 2]

#
# Complete the 'hurdleRace' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height
#

# k is starting jump height: 1
# height is an array of hurdle lengths: [1,2,5,6,4,3]


def hurdleRace(k, height):
    highest = max(height)
    if highest < k:
        return(0)
    else:
        return(highest - k)


hurdleRace(k, height)
