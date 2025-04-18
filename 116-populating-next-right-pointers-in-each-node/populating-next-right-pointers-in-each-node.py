"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        
        if not root:
            return None

        level = root

        while level.left:
            curr = level
            while curr:
                curr.left.next = curr.right

                if curr.next:
                    curr.right.next = curr.next.left
                
                curr = curr.next

            level = level.left

        return root

        