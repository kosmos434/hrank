# 🐦🐦

arr = [1, 1, 2, 2, 3]


# count the instances of each bird type
# return the lowest id number with highest count

def migratoryBirds(arr):
    highest = 0
    scoreDict = {}
    newArr = list(set(arr))
    for i in newArr:
        count = arr.count(i)
        if count > highest:
            highest = count
        scoreDict[i] = count
    # print(scoreDict)
    for key, val in scoreDict.items():
        if val == highest:
            return(key)


migratoryBirds(arr)
