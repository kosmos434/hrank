# 🐊
#
# Complete the 'getNode' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER positionFromTail
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def getNode(llist, positionFromTail):
    depthIntoList = 0
    temp = llist
    # sounding out the depth of the linked list
    while temp.next != None:
        temp = temp.next
        depthIntoList += 1
    temp = llist  # reset temp to og head
    # now going to the node specified by positionFromTail
    for i in range(depthIntoList - positionFromTail):
        temp = temp.next
    return temp.data
