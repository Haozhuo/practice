# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#T(n) = 2*T(n/2) + O(1)
#T(n) = O(nlogn)
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        s,e,mid=0,len(lists),(0+len(lists))/2
        n1 = self.mergeKLists(lists[s:mid])
        n2 = self.mergeKLists(lists[mid:e])
        return self.merge(n1,n2)

    def merge(self,n1,n2):
        dummy = ListNode(0)
        l = dummy
        l1,l2 = n1,n2
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                l.next = ListNode(l1.val)
                l1 = l1.next
            else:
                l.next = ListNode(l2.val)
                l2 = l2.next

            l = l.next

        if l1 == None:
            while l2 != None:
                l.next = ListNode(l2.val)
                l = l.next
                l2 = l2.next

        elif l2 == None:
            while l1 != None:
                l.next = ListNode(l1.val)
                l = l.next
                l1 = l1.next

        return dummy.next
