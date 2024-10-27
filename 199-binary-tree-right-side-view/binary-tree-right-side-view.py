# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []

        if not root:
            return res

        q = collections.deque()
        q.append(root)

        while q:
            rightMost = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightMost = node
                    q.append(node.left)
                    q.append(node.right)
            
            if rightMost:
                res.append(rightMost.val)

        return res 
        