# 🧸
k = 50
prices = [1, 12, 5, 200, 1000, 10]


def maximumToys(prices, k):
    acc = 0
    i = 0
    toys = 0
    prices.sort()
    while acc <= k:
        acc += prices[i]
        if acc <= k:
            toys += 1
        i += 1
    return(toys)


maximumToys(prices, k)
