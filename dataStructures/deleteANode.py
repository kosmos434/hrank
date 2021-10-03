# ❌

#
# Complete the 'deleteNode' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def deleteNode(llist, position):
    if not position:
        return llist.next

    currPosition = 0
    prevNode = None
    currNode = llist

    while currPosition < position:
        prevNode = currNode
        currNode = currNode.next
        currPosition += 1
    # taking out the current node at specified position
    # and bridging the gap with prev.next = curr.next
    # so like 1,2,3
    # del 2:
    # 2.next is 3
    # set 1.next to that
    prevNode.next = currNode.next

    return llist
