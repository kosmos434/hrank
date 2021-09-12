# 🐭🐱

x = 1
y = 2
z = 3


def catAndMouse(x, y, z):
    catADistance = abs(x-z)
    catBDistance = abs(y-z)
    if catADistance < catBDistance:
        return('Cat A')
    if catADistance > catBDistance:
        return('Cat B')
    if catADistance == catBDistance:
        return('Mouse C')


catAndMouse(x, y, z)
