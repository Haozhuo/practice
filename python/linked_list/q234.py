"""
Given a singly linked list, determine if it is a palindrome.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next ,slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while slow != None:
            if slow.val != rev.val:
                return False
            slow = slow.next
            rev = rev.next
        return True
