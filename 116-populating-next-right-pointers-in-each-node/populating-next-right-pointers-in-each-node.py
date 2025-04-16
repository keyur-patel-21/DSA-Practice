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

        q = collections.deque()
        q.append(root)

        while q:
            level = len(q)
            for i in range(level):
                curr = q.popleft()
                if i != level - 1:
                    curr.next = q[0]
                if curr.left:
                    q.append(curr.left)
                    q.append(curr.right)


        return root
        