# 🖇🖇


def reverse(list):
    curr = list
    next = list
    while list:
        next = list.next
        curr = list
        list.next, list.prev = list.prev, list.next
        list = next
    return curr
