# ☁🌧
c = [0, 0, 0, 1, 0, 0]


def jumpingOnClouds(c):
    index = 0
    jumps = 0
    while index < len(c)-1:
        if index < len(c) - 2 and c[index + 2] == 0:
            index += 2
        else:
            index += 1
        jumps += 1
        # print(c[index])
    # print("jumps", jumps)
    return jumps


jumpingOnClouds(c)
