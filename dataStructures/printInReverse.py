# 🖨

def reversePrint(llist):
    data = []
    while llist:
        data.append(llist.data)
        llist = llist.next

    data.reverse()
    for i in data:
        print(i)
