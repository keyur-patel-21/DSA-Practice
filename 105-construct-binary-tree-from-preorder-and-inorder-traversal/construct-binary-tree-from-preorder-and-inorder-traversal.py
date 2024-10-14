
class Solution(object):
    def buildTree(self, preorder, inorder):
        midIdx = {}
        for i, n in enumerate(inorder):
            midIdx[n] = i 
        if not (preorder or inorder):
            return None
        root = TreeNode(preorder[0])
        mid = midIdx[preorder[0]]
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
        