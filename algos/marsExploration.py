# 🤖

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

s = 'SOSOOSOSOSOSOSSOSOSOSOSOSOS'


def marsExploration(s):
    # this works unless the string is like 'ooo sss ooo'
    # newNum = len(s)
    # countS = s.count('S')
    # countO = s.count('O')
    # print(newNum - countO - countS)

    wrongCount = 0
    parts = [s[i:i+3] for i in range(0, len(s), 3)]
    for i in parts:
        if i[0] != 'S':
            wrongCount += 1
        if i[1] != 'O':
            wrongCount += 1
        if i[2] != 'S':
            wrongCount += 1
    return(wrongCount)


marsExploration(s)
