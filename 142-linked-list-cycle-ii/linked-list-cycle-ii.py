# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Approach:
1. Use Floyd's Cycle Detection Algorithm (Tortoise and Hare approach).
2. Initialize two pointers: `slow` moves one step at a time, `fast` moves two steps.
3. If there is a cycle, `slow` and `fast` will eventually meet inside the loop.
4. Once a cycle is detected, reset `slow` to head and move both `slow` and `fast` 
   one step at a time until they meet again. The meeting point is the start of the cycle.
5. If no cycle is detected, return None.

Time Complexity: O(N)
- In the worst case, we traverse the linked list twice: 
  * Once to detect the cycle (O(N))
  * Once to find the start of the cycle (O(N))
  * Overall, it's O(N).

Space Complexity: O(1)
- We use only two pointers (`slow` and `fast`), so no extra space is used.
"""

class Solution(object):
    def detectCycle(self, head):
        
        slow, fast = head, head
        isCycle = False

        while (fast != None and fast.next != None): # Using 'and' ensures both pointers remain valid
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                isCycle = True
                break
        
        if isCycle:
            slow = head
            
            while (slow != fast):
                slow = slow.next
                fast = fast.next
        
            return slow
        return None
