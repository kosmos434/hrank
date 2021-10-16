# 🪑

s = 'AAABBB'


def alternatingCharacters(s):
    deletions = 0
    for i in range(len(s) - 1):
        if s[i+1] == s[i]:
            deletions += 1
    return(deletions)


alternatingCharacters(s)
