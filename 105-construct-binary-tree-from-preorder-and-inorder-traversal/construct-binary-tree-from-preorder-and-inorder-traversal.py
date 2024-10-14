class Solution(object):
    def buildTree(self, preorder, inorder):
        # Hashmap to store the index of values in the inorder traversal
        midIdx = {n: i for i, n in enumerate(inorder)}
        
        # Helper function to build the tree using preorder and inorder indices
        def helper(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None

            # The first element in preorder is always the root
            root_val = preorder[pre_left]
            root = TreeNode(root_val)

            # Get the index of the root in inorder traversal
            mid = midIdx[root_val]
            
            # Number of nodes in the left subtree
            left_subtree_size = mid - in_left

            # Recursively build the left and right subtrees
            root.left = helper(pre_left + 1, pre_left + left_subtree_size, in_left, mid - 1)
            root.right = helper(pre_left + left_subtree_size + 1, pre_right, mid + 1, in_right)
            
            return root
        
        # Call the helper with initial indices for the full range
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
