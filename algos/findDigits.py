# 🔎

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

n = 10


def findDigits(n):
    divisors = 0
    for i in [int(j) for j in str(n)]:
        if i == 0:
            continue
        if n % i == 0:
            divisors += 1
    return(divisors)


findDigits(n)
