# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Approach:
# 1. Find the middle of the linked list using the slow and fast pointer approach.
# 2. Reverse the second half of the linked list.
# 3. Merge the first half and the reversed second half alternatively.

# Time Complexity (TC): O(N) 
# - Finding the middle takes O(N/2) = O(N).
# - Reversing the second half takes O(N/2) = O(N).
# - Merging the two halves takes O(N).
# - Overall: O(N) + O(N) + O(N) = O(N).

# Space Complexity (SC): O(1)
# - We only use a few pointers (slow, fast, pre, cur, etc.), so the space is constant.

class Solution(object):
    def reorderList(self, head):
        
        slow, fast = head, head

        # Step 1: Find the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        second = slow.next
        slow.next = None  # Cut the first half
        
        pre, cur = None, second
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        # Step 3: Merge the two halves
        fast, slow = head, pre
        while slow:
            tmp1, tmp2 = fast.next, slow.next
            fast.next = slow
            slow.next = tmp1
            fast = tmp1
            slow = tmp2
