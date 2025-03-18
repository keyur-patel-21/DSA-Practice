# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        inorderMap = {n:i for i, n in enumerate(inorder)}
        
        def helper(start, end):
            if start > end:
                return None

            rootVal = postorder.pop()
            rootIndex = inorderMap[rootVal]

            root = TreeNode(rootVal)

            root.right = helper(rootIndex + 1, end)
            root.left = helper(start, rootIndex - 1)

            return root

        return helper(0, len(inorder)-1)