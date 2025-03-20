# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Approach:
1. Use two pointers (`curA` and `curB`), starting at `headA` and `headB` respectively.
2. Traverse both lists simultaneously.
   - If `curA` reaches the end, move it to `headB`.
   - If `curB` reaches the end, move it to `headA`.
3. Since both pointers traverse the same total length (A + B), they will eventually meet at the intersection node.
4. If there is no intersection, both pointers will reach `None` at the same time, returning `None`.

Time Complexity: O(N + M)
- Each pointer traverses at most `N + M` steps, where `N` and `M` are the lengths of the two linked lists.

Space Complexity: O(1)
- Only two pointers (`curA` and `curB`) are used, so no extra space is required.
"""

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
            
        curA, curB = headA, headB

        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA

        return curA
