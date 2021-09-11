# b/w 2 sets 👀

a = [2, 4]
b = [16, 32, 96]

# so the a's have to be a factor of it
# and it has to be a factor of b's


def getTotalX(a, b):
    numInts = 0
    afactors = []
    bfactors = []

    # Write your code here
    for i in range(max(b)):
        if all((thing % (i+1) == 0) for thing in b):  # if
            bfactors.append(i+1)
    for i in bfactors:
        if all(((i % thing) == 0) for thing in a):
            afactors.append(i)

    # print(bfactors)
    # print(afactors)
    return(len(afactors))


getTotalX(a, b)
