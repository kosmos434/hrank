# 🦹‍♂️

n = 3
m = 7
s = 3


def saveThePrisoner(n, m, s):
    numPrisoners = n
    numCandy = m
    startSeat = s
    endSeat = startSeat

    # for i in range(numCandy):
    #     endSeat = ((i + startSeat) % numPrisoners)
    #     # print(endSeat)

    endSeat = (startSeat + numCandy - 1) % numPrisoners
    if endSeat == 0:
        endSeat = numPrisoners
    return(endSeat)


saveThePrisoner(n, m, s)
