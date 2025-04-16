# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        self.first = None
        self.second = None
        self.prev = TreeNode(float("-inf"))

        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if self.prev.val > root.val:
                if not self.first:
                    self.first = self.prev
                    self.second = root
                else:
                    self.second = root

            self.prev = root
            root = root.right

        self.first.val, self.second.val = self.second.val, self.first.val 
        