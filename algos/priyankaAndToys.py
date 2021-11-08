# 🧸

w = [16, 18, 10, 13, 2, 9, 17, 17, 0, 19]


def toys(w):
    w = sorted(w)
    print(w)
    containers = 1
    prev = w[0]
    for i in w[1:]:
        if (i - prev) > 4:
            containers += 1
            prev = i
    return(containers)


toys(w)
