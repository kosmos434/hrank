# 1 index based btw

p = [5, 2, 1, 3, 4]
# returns this [4, 2, 5, 1, 3]


def permutationEquation(p):
    returnArray = []
    for i in range(1, len(p)+1):  # shift to 1 index based
        loc = p.index(i) + 1  # shift to 1 index again
        print(loc)
        locOfThat = p.index(loc) + 1
        # print(locOfThat)
        returnArray.append(locOfThat)
    return(returnArray)


permutationEquation(p)
