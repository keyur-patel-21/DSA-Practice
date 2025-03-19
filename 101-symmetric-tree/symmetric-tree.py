# Time Complexity: O(N) 
# - Each node in the tree is visited once in a depth-first traversal.
#
# Space Complexity: O(H) 
# - The recursion stack takes up to O(H) space, where H is the height of the tree.
# - In the worst case (skewed tree), H = N, leading to O(N) space complexity.
# - In the best case (balanced tree), H = log(N), leading to O(log N) space complexity.
#
# Approach:
# - Use a recursive depth-first search (DFS) to compare the left and right subtrees.
# - Base cases:
#   - If both left and right are None, return True.
#   - If one is None and the other is not, return False.
# - Check whether the current nodes have the same value.
# - Recursively compare:
#   - The left subtree of the left node with the right subtree of the right node.
#   - The right subtree of the left node with the left subtree of the right node.

class Solution(object):
    def isSymmetric(self, root):
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False

            return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)
        
        return dfs(root.left, root.right)
