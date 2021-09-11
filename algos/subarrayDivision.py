# 🍫

s = [1, 2, 1, 3, 2]
d = 3
m = 2


# so s is a numbered chocolate bar (weird)
# that we divide into -m- long arrays
# and the ints on them must add to -d-


def birthday(s, d, m):
    score = 0
    endOffset = m-1
    for i in range(len(s) - endOffset):
        runningTally = 0
        # print(i)
        for j in range(i, i+m):
            # print(j)
            runningTally += s[j]
        # print(runningTally)
        if runningTally == d:
            score += 1
    return(score)


birthday(s, d, m)
