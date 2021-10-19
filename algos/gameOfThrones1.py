# 🤴

from collections import Counter
s = 'aaabbbb'


def gameOfThrones(s):
    # # so if it's even, check to make sure it's all pairs
    #   if len(s) % 2 == 0:
    #       for i in s:
    #           if s.count(i) % 2 != 0:
    #               print("NO")
    #               return
    #       print("YES")
    #       return

    # # if it's odd, check that it's all pairs and one loner
    #   else:
    #       lonerCheck = False
    #       # print("It's odd")
    #       for i in s:
    #           if s.count(i) % 2 != 0:
    #               if s.count(i) == 1:
    #                   if lonerCheck:
    #                       print("NO")
    #                       return
    #                   else:
    #                       lonerCheck = True
    #               else:
    #                   print("NO")
    #                   return
    #       print("YES")

    # let's try by odd pairs
    # if there's more than 1 odd, no palindrome
    frequency = Counter(s)
    oddCounts = 0
    for i in frequency.values():
        if i % 2 != 0:
            oddCounts += 1
    if oddCounts > 1:
        return "NO"
    else:
        return "YES"


gameOfThrones(s)
