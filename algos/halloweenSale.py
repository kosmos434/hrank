# 👻🎃🦇
# I am not proud of this one

p = 100
d = 19
m = 1
s = 180


def howManyGames(p, d, m, s):
    if p > s:
        return 0
    price = p
    discount = d
    minumum = m
    budget = s
    prices = []

    while budget > 0:
        prices.append(price)
        if (price - discount) > minumum:
            price = (price-discount)
        else:
            price = minumum
        budget -= price

    gameCount = 0
    # print(prices)
    acc = 0
    for i in prices:
        if (acc + i) <= s:
            acc = acc + i
            # print(acc)
            gameCount += 1
        else:
            break

    return(gameCount)


howManyGames(p, d, m, s)
