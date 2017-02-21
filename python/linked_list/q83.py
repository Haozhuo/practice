"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head == None or head.next == None:
        return head
    prev = head
    curr = head.next

    while curr != None:
        if prev.val == curr.val:
            prev.next = curr.next
            del curr
            curr = prev.next
        else:
            prev = prev.next
            curr = curr.next

    return head
