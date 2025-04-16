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

        def helper(root):
            # base
            if not root:
                return
            # logic

            # left
            helper(root.left)

            # current
            if self.prev.val > root.val:
                if not self.first:
                    self.first = self.prev
                    self.second = root
                else:
                    self.second = root

            self.prev = root

            # right
            helper(root.right)
                




        helper(root)
        self.first.val, self.second.val = self.second.val, self.first.val 
        