# 🔌💡⚡

b = 60
keyboards = [40, 50, 60]
drives = [5, 8, 12]


def getMoneySpent(keyboards, drives, b):
    highest = -1
    for i in keyboards:
        for j in drives:
            if i + j <= b and i + j >= highest:
                highest = i + j

    # if highest == 0:
    #     highest = max([max(keyboards), max(drives)])
    return(highest)


getMoneySpent(keyboards, drives, b)
