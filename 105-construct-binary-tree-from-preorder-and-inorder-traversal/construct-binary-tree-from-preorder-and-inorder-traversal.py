# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.idx = 0
        self.inorderMap = {}

    def buildTree(self, preorder, inorder):
        self.inorderMap = {n:i for i, n in enumerate(inorder)}
        return self.helper(preorder, 0, len(inorder)-1)

    def helper(self, preorder, start, end):
        if start>end:
            return None

        root = TreeNode(preorder[self.idx])
        rootIdx = self.inorderMap[preorder[self.idx]]
        self.idx += 1

        root.left = self.helper(preorder, start, rootIdx - 1)
        root.right = self.helper(preorder, rootIdx+1, end)

        return root
        


