

# Approach:
# - The problem requires reconstructing a binary tree given its preorder and inorder traversals.
# - We use a recursive approach with a hashmap (`inorderMap`) for quick lookup of indices in the inorder traversal.
# - The `idx` variable keeps track of the current node in the preorder list.
# - The root node is always the first element in the preorder list.
# - Using `inorderMap`, we find the root's index in `inorder` and recursively build the left and right subtrees.
# - The left subtree is constructed from `start` to `rootIdx - 1`, and the right subtree from `rootIdx + 1` to `end`.

# Time Complexity: O(N)
# - Constructing the `inorderMap` takes O(N).
# - Each node is processed once, and the hashmap allows O(1) lookup for root index.
# - The recursive function processes each node once, leading to O(N) overall complexity.

# Space Complexity: O(N)
# - The hashmap `inorderMap` stores N elements (O(N) space).
# - The recursive call stack takes O(N) space in the worst case (skewed tree) and O(log N) for a balanced tree.
# - Thus, worst-case space complexity is O(N).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def __init__(self):
        self.idx = 0
        self.inorderMap = {}

    def buildTree(self, preorder, inorder):
        self.inorderMap = {n: i for i, n in enumerate(inorder)}
        return self.helper(preorder, 0, len(inorder) - 1)

    def helper(self, preorder, start, end):
        if start > end:
            return None

        root = TreeNode(preorder[self.idx])
        rootIdx = self.inorderMap[preorder[self.idx]]
        self.idx += 1

        root.left = self.helper(preorder, start, rootIdx - 1)
        root.right = self.helper(preorder, rootIdx + 1, end)

        return root



