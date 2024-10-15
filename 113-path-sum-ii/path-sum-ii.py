# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        res = []
        sumOfPath = 0
        curPath = []

        def dfs(root, res, sumOfPath, curPath, targetSum):
            if not root:
                return None

            sumOfPath += root.val
            curPath.append(root.val)

            if not root.left and not root.right and sumOfPath == targetSum:
                res.append(curPath[:])
            
            dfs(root.left, res, sumOfPath, curPath, targetSum)
            dfs(root.right, res, sumOfPath, curPath, targetSum)

            sumOfPath -= root.val
            curPath.pop()

        dfs(root, res, sumOfPath, curPath, targetSum )
        return res