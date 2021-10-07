# 🖇🖇🖇🖇🖇


def mergeLists(head1, head2):
    curr = SinglyLinkedListNode(9999)
    NEWHEAD = curr

    # now iterate through them both, checking all the way

    while head1 and head2:

        if head1.data <= head2.data:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next

        if head1 == None:
            curr.next = head2
            break
        if head2 == None:
            curr.next = head1
            break

    return NEWHEAD.next
