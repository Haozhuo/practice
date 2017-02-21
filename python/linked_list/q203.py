"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def removeElements(self, head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    if head == None:
        return head

    prev = head
    curr = head.next

    while curr != None:
        if curr.val == val:
            prev.next = curr.next
            del curr
            curr = prev.next
        else:
            prev = prev.next
            curr = curr.next

    if head.val == val:
        if head.next == None:
            del head
            head = None
        else:
            temp = head.next
            head = temp

    return head
