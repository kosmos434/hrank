# 🧵
s = 'hacakaeararanaka'


def hackerrankInString(s):
    hrank = 'hackerrank9'
    for i in s:
        if i == hrank[0]:
            hrank = hrank[1:]
    if hrank == '9':
        return("YES")
    return('NO')


hackerrankInString(s)
