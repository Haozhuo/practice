"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    dummy = ListNode(0)
    dummy.next = head

    f = dummy
    s = dummy

    for i in range(0,n+1):
        f = f.next
    while(f != None):
        f = f.next
        s = s.next

    temp = s.next
    s.next = s.next.next
    del temp
    return dummy.next
