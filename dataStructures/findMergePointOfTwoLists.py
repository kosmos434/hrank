# 🖇

def findMergeNode(head1, head2):
    dataSet = set()
    while head1:
        dataSet.add(head1)
        head1 = head1.next

    while head2:
        if head2 in dataSet:
            return head2.data
        head2 = head2.next


findMergeNode(head1, head2)
