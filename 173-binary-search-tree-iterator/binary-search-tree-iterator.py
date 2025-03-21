# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach:
# The BSTIterator class implements an in-order traversal iterator for a binary search tree (BST). 
# It uses an explicit stack to simulate the recursive traversal of the tree. 
# - The constructor (`__init__`) initializes the stack with all the leftmost nodes of the tree.
# - The `next()` function pops the top element from the stack, processes it, and pushes the leftmost 
#   nodes of the right subtree (if any) onto the stack.
# - The `hasNext()` function simply checks if the stack is non-empty, indicating more nodes remain.

# Time Complexity:
# - `__init__()`: O(h) in the worst case (where h is the height of the BST), as it pushes all left nodes.
# - `next()`: O(1) on average. Each node is pushed and popped from the stack exactly once.
# - `hasNext()`: O(1) since it only checks if the stack is non-empty.
# Overall, the amortized time complexity for all `next()` calls is O(n), where n is the number of nodes.

# Space Complexity:
# - O(h) in the worst case due to the stack storing at most h nodes, where h is the height of the BST.
# - For a balanced BST, h = O(log n), leading to O(log n) space.
# - For a skewed BST, h = O(n), leading to O(n) space.

class BSTIterator(object):

    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
        

    def next(self):
        res = self.stack.pop()
        if res.right:
            cur = res.right
            while cur:
                self.stack.append(cur)
                cur = cur.left

        return res.val
                 

    def hasNext(self):
        return len(self.stack) != 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
