# 🤡

s = 'acxz'


def funnyString(s):
    r = s[::-1]
    # print(r)

    # first list of ord abses
    first = []
    for i in range(1, len(s)):
        first.append(abs(ord(s[i]) - ord(s[i-1])))
    # print("first", first)

    second = []
    for i in range(1, len(r)):
        second.append(abs(ord(r[i]) - ord(r[i-1])))

    # print("second", second)

    return("Funny" if first == second else "Not Funny")


funnyString(s)
