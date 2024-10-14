# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
            def dfs(node, sum):
                if not node:
                    return False

                sum =  sum + node.val
                if not node.right and not node.left:
                    return sum == targetSum
                return (dfs(node.right, sum) or dfs(node.left, sum))

            return dfs(root, 0)