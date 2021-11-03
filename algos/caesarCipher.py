# 👑

s = 'Always-Look-on-the-Bright-Side-of-Life'
k = 5


def caesarCipher(s, k):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    newStr = ''
    for i in s:
        if i.lower() in alpha:
            # this is bad
            if i.islower():
                newStr += chr((ord(i) - ord('a') + k) % 26 + ord('a'))
            else:
                newStr += chr((ord(i) - ord('A') + k) % 26 + ord('A'))
        else:
            newStr += i
    return(newStr)


caesarCipher(s, k)
