# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow, fast = head, head
        isCycle = False

        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                isCycle = True
                break
        
        # slow = head
        # while(slow != fast):
        #     slow = slow.next
        #     fast = fast.next
        
        return isCycle

        