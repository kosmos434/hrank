# 🔗🔗🔗🔗

def compare_lists(llist1, llist2):
    while llist1 or llist2:
        if not llist1 or not llist2:
            return 0
        if llist1.data != llist2.data:
            return 0
        llist1 = llist1.next
        llist2 = llist2.next
    return 1
