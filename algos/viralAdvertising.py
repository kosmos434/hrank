# 🦠🔬

import math
n = 5


def viralAdvertising(n):
    total = 0
    liked = 0
    recipients = 5
    for i in range(n):
        liked = math.floor(recipients/2)
        total += liked
        recipients = liked * 3
    return total


viralAdvertising(n)
