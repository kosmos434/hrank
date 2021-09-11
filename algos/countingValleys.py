# 🗻🗻


def countingValleys(steps, path):
    seaLevel = 0
    valleys = 0
    for i in path:
        if i == 'D':
            seaLevel -= 1
        if i == 'U':
            seaLevel += 1
            # after that, if we're going up
            # and the sea level is now zero,
            # we're exting a valley
            if seaLevel == 0:
                valleys += 1

    return valleys
