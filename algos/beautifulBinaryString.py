# 1010

b = '0101010'


def beautifulBinaryString(b):
    # uglies = 0
    # for i in range(1, len(b)):
    #     if b[i] == '1':
    #         if b[i - 1] == '0' and b[i + 1] == '0':
    #             uglies += 1
    # print(uglies)

    # smarter way 🧠
    return(b.count('010'))


beautifulBinaryString(b)
