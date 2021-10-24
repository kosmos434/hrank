# 🎂

calorie = [5, 10, 7]


def marcsCakewalk(calorie):
    total = 0
    calorie = sorted(calorie, reverse=True)
    for i in range(len(calorie)):
        total += (2**i) * (calorie[i])
    return(total)


marcsCakewalk(calorie)
