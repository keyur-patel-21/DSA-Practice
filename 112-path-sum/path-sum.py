# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        def dfs(node, currentSum):
            if not node:
                return False
            
            currentSum += node.val
            
            # Check if it's a leaf node and if the current sum matches the target sum
            if not node.left and not node.right:
                return currentSum == targetSum
            
            # Recur for left and right subtrees
            return dfs(node.left, currentSum) or dfs(node.right, currentSum)

        return dfs(root, 0)
