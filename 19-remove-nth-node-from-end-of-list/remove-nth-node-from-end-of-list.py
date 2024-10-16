# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        dummy.next = head
        l, r = dummy, head

        while n > 0:
            r = r.next
            n -= 1

        while r:
            r = r.next
            l = l.next

        l.next = l.next.next
        return dummy.next
        