# 🍰

candles = [4, 4, 1, 3]


def birthdayCakeCandles(candles):
    candleTally = 0
    # Write your code here
    candles.sort()
    for i in range(len(candles)):
        if candles[i] == candles[-1]:
            candleTally += 1
    return candleTally


birthdayCakeCandles(candles)
