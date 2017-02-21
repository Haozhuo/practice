"""
Reverse a singly linked list.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #iterative approach
        if head == None or head.next == None:
            return head

        prev = head
        curr = head.next
        head.next = None

        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #recursive approach
        if head == None or head.next == None:
            return head

        ret = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return ret
