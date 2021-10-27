# 🧵

import math
s = 'abcac'
n = 10


def repeatedString(s, n):
    aCount = s.count('a')
    stringLength = len(s)
    factors = math.floor(n / stringLength)
    remainder = n % stringLength
    stringRemainder = s[:remainder]
    aCountInRemainder = stringRemainder.count('a')

    total = (aCount * factors) + aCountInRemainder
    return(total)


repeatedString(s, n)
