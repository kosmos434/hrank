# 🍫

n = 10
c = 2
m = 5


def chocolateFeast(n, c, m):
    eaten = 0
    wrapper = 0
    while n >= c:
        n -= c
        eaten += 1
        wrapper += 1

        if wrapper == m:
            eaten += 1
            wrapper = 1

    return(eaten)


chocolateFeast(n, c, m)
