# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow, fast = head, head
        flag = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                flag = True
                break
        if not flag:
            return None
        if flag:
            fast = head
            while(fast != slow):
                slow = slow.next
                fast = fast.next
            return slow

        

        