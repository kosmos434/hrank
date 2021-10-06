# 🔗🔗🔗🔗

def reverse(llist):

    curr = llist
    prev = None
    nexted = None

    while curr:
        nexted = curr.next
        curr.next = prev
        prev = curr
        curr = nexted
    return prev
