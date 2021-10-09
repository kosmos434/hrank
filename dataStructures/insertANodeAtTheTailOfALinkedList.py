# 🔗🔗🔗

def insertNodeAtTail(head, data):
    if head == None:
        return SinglyLinkedListNode(data)

    curr = head
    while curr.next:
        curr = curr.next
    curr.next = SinglyLinkedListNode(data)
    return head
