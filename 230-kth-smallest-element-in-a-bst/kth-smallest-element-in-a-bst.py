# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        stack = []
        count = 0

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            count += 1

            if count == k:
                return root.val

            root = root.right
        