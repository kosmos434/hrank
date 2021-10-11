# long title oops

def insertNodeAtPosition(llist, data, position):
    curr = llist
    for i in range(position):
        prev = curr
        curr = curr.next
    newNode = SinglyLinkedListNode(data)
    prev.next = newNode
    newNode.next = curr

    return llist
