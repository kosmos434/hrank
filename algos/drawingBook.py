# 📚


n = 6
p = 2


def pageCount(n, p):
    lower = 0
    book = []
    for i in range(0, n+1, 2):
        book.append((i, i+1))
    # print(book)

    # # going forwards
    for i in range(len(book)):
        # print(book[i])
        if p in book[i]:
            lower = i
            # print("bingo")

    # going backwards
    book.reverse()
    for i in range(len(book)):
        # print(book[i])
        if p in book[i]:
            if i < lower:
                lower = i
                # print("bingo")

    return(lower)


pageCount(n, p)
