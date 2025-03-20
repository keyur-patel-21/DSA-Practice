# Approach:
# 1. Create a dummy node pointing to the head of the linked list. This helps in edge cases like removing the first node.
# 2. Use two pointers, `slow` and `fast`, both starting from the dummy node.
# 3. Move the `fast` pointer `n+1` steps ahead to maintain a gap of `n` nodes between `slow` and `fast`.
# 4. Move both `slow` and `fast` pointers one step at a time until `fast` reaches the end.
# 5. At this point, `slow` is just before the node to be removed. Update `slow.next` to skip the target node.
# 6. Return `dummy.next`, which points to the modified head of the list.

# Time Complexity (TC): O(L) - We traverse the linked list at most twice (once to move `fast`, once to find `slow`).
# Space Complexity (SC): O(1) - We use only a constant amount of extra space.

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        dummy.next = head

        slow, fast = dummy, dummy
        count = 0

        while count <= n:
            fast = fast.next
            count += 1

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
    
        return dummy.next
