# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
        def sortList(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            if head == None or head.next == None:
                return head

            h1, h2 = head, head.next

            while h2 != None and h2.next != None:
                h1 = h1.next
                h2 = h2.next.next

            temp = h1.next
            h1.next = None
            h1 = self.sortList(head)
            h2 = self.sortList(temp)
            return self.merge(h1, h2)

        def merge(self, h1, h2):
            dummy = ListNode(0)
            head = dummy
            while h1 != None and h2 != None:
                if h1.val <= h2.val:
                    head.next = ListNode(h1.val)
                    h1 = h1.next
                else:
                    head.next = ListNode(h2.val)
                    h2 = h2.next

                head = head.next

            if h1 == None:
                while h2 != None:
                    head.next = ListNode(h2.val)
                    head = head.next
                    h2 = h2.next
            else:
                while h1 != None:
                    head.next = ListNode(h1.val)
                    head = head.next
                    h1 = h1.next

            return dummy.next
