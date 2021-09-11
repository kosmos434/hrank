# 🦘

# do the roo meet up
x1 = 4523
v1 = 8092
x2 = 9419
v2 = 8076


def kangaroo(x1, v1, x2, v2):
    # first roo starts at x1 and moves right by v1
    # second roo starts at x2 and moves right by v2

    while x1 < 2000000000:  # just add more zeroes 🧠
        if x1 == x2:
            print("YES")
        x1 += v1
        x2 += v2
    return("NO")


kangaroo(x1, v1, x2, v2)
