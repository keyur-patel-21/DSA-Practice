# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach:
# The function computes the sum of all root-to-leaf numbers in a binary tree.
# - We use a recursive DFS approach where we traverse the tree while building the current number.
# - At each node, we multiply the accumulated number by 10 and add the node’s value.
# - If we reach a leaf node (no left or right child), we return the computed number.
# - Otherwise, we sum up the values obtained from the left and right subtrees.

# Time Complexity (TC):
# - Since we visit each node exactly once, the time complexity is **O(N)**, 
#   where N is the number of nodes in the tree.

# Space Complexity (SC):
# - The space complexity is **O(H)**, where H is the height of the tree.
# - In the worst case (skewed tree), H = O(N), making the space complexity **O(N)**.
# - In a balanced tree, H = O(log N), making the space complexity **O(log N)**.

class Solution(object):
    def sumNumbers(self, root):
        def sum(root, digit):
            if not root:
                return 0

            digit = (digit * 10) + root.val

            if not root.left and not root.right:
                return digit
            
            return sum(root.left, digit) + sum(root.right, digit)

        return sum(root, 0)
