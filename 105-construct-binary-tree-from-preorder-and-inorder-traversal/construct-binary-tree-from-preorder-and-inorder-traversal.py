# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])

        rootIdx = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:rootIdx+1], inorder[:rootIdx])
        root.right = self.buildTree(preorder[rootIdx+1:], inorder[rootIdx+1:])

        return root