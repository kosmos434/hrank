# 🚗🚗

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def minimumDistances(a):
    default = -1
    lowestDistance = []
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            # print(a[i], a[j])
            # print("Honk: ", abs(i - j))
            if a[i] == a[j]:
                numb = abs(i - j)
                lowestDistance.append(numb)
    if lowestDistance:
        return(min(lowestDistance))
    else:
        return(default)


minimumDistances(a)
