# Approach:
# The function checks whether a given binary tree is a valid Binary Search Tree (BST).
# It uses a recursive helper function `valid` that ensures:
# 1. Each node's value lies within a valid range (left < node.val < right).
# 2. The left subtree must have values less than the current node.
# 3. The right subtree must have values greater than the current node.
# The function recursively updates the valid range for each subtree.

# Time Complexity (TC): O(N) 
# - Each node is visited once, making the complexity linear.

# Space Complexity (SC): O(H)
# - The recursive call stack takes O(H) space, where H is the height of the tree.
# - In the worst case (skewed tree), H = O(N), leading to O(N) space complexity.
# - In the best case (balanced tree), H = O(log N), leading to O(log N) space complexity.
# Definition for a binary tree node.


# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def valid (root, left, right):
            if not root:
                return True
            if not (left < root.val < right):
                return False
            
            
            return valid(root.left, left, root.val) and valid(root.right, root.val, right)

        return valid(root, float("-inf"), float("inf"))        