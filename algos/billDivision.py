# 💸

bill = [3, 10, 2, 9]
k = 1
b = 12


def bonAppetit(bill, k, b):
    total = sum(bill)
    karenShare = (total - bill[k])/2

    actual = b-karenShare
    if actual:
        print(str(actual).rstrip('.0'))
    else:
        print('Bon Appetit')


bonAppetit(bill, k, b)
