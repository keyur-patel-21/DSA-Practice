# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        pathP = []
        pathQ = []

        def helper(root, p, q, path):
            # base
            if not root:
                return False

            # logic
            path.append(root)

            if root == p:
                pathP.extend(path[:])
                pathP.append(root)

            if root == q:
                pathQ.extend(path[:])
                pathQ.append(root)

            if pathP and pathQ:     #if both path found, STOP Recursive call
                return True

            found = helper(root.left, p, q, path) or helper(root.right, p, q, path)
            
            path.pop()
            return found

        helper(root, p, q, [])
        for i in range(len(pathP)):
            if pathP[i] != pathQ[i]:
                return pathP[i-1]
            
        