"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    #inplace
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = curr = ListNode(0)
        dummy.next = l1
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                l1 = l1.next
            else:
                temp1 = curr.next
                temp2 = l2.next
                curr.next = l2
                l2.next = temp1
                l2 = temp2

            curr = curr.next
        curr.next = l1 or l2
        return dummy.next

    #extra memory
    def mergeTwoLists2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = curr = ListNode(0)
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                curr.next = ListNode(l1.val)
                l1 = l1.next
            else:
                curr.next = ListNode(l2.val)
                l2 = l2.next
            curr = curr.next

        if l1 == None:
            curr.next = l2
        else:
            curr.next = l1
        return dummy.next
