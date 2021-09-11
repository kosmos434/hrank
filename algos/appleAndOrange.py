# 🍎 🍊


def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    appleHit = 0
    orangeHit = 0
    hitRange = range(s, t+1)

    for i in apples:
        if (a + i) in hitRange:
            appleHit += 1
    for i in oranges:
        if (b + i) in hitRange:
            orangeHit += 1
    print(appleHit)
    print(orangeHit)
