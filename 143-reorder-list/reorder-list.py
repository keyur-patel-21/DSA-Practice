# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second  = slow.next
        slow.next = None

        pre = None
        cur = second
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        
        slow = pre
        fast = head

        while slow:
            tmp1, tmp2 = fast.next, slow.next
            fast.next = slow
            slow.next = tmp1
            fast = tmp1
            slow = tmp2

        