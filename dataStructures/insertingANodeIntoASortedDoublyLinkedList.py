# ⏩⏪
# incomplete

def sortedInsert(llist, data):
    curr = llist
    newNode = DoublyLinkedListNode(data)

    while curr.next:
        prev = curr

        if data < curr.next.data:
            prev.next = newNode
            curr = curr.next
            curr.prev = newNode
            return llist

        curr = curr.next
