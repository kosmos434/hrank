

# plus minus 🐒🐒

arr = [-4, 3, -9, 0, 4, 1]


def plusMinus(arr):
    # 🙈🙉🙊
    numItems = len(arr)
    highs = 0
    lows = 0
    zeroes = 0

    for i in range(numItems):
        if (arr[i] > 0):
            highs += 1
        if (arr[i] < 0):
            lows += 1
        if (arr[i] == 0):
            zeroes += 1

    # then print the ratios out
    print("{:.6f}".format(highs/numItems))
    print("{:.6f}".format(lows/numItems))
    print("{:.6f}".format(zeroes/numItems))


plusMinus(arr)
