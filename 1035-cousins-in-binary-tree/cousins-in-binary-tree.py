# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach:
# - We use a BFS (level-order traversal) approach with a queue (q) to traverse the tree level by level.
# - Another queue (pq) keeps track of parent nodes for each node in q.
# - We iterate level by level, checking if x and y are found at the same level.
# - If both are found in the same level and have different parents, return True (they are cousins).
# - If one is found but not the other, return False.
# - If the loop ends without finding both, return False.

# Time Complexity (TC): O(N)
# - Each node is processed once in a BFS traversal, leading to O(N) complexity.

# Space Complexity (SC): O(N)
# - In the worst case (a completely unbalanced tree), we store O(N) nodes in the queue.

import collections

class Solution(object):
    def isCousins(self, root, x, y):
        q = collections.deque()
        pq = collections.deque()

        q.append(root)
        pq.append(None)

        x_found, y_found = False, False
        x_parent, y_parent = None, None

        while q:
            for i in range(len(q)):
                node = q.popleft()
                parent = pq.popleft()

                if node.val == x:
                    x_found = True
                    x_parent = parent

                if node.val == y:
                    y_found = True
                    y_parent = parent

                if node.left:
                    q.append(node.left)
                    pq.append(node)

                if node.right:
                    q.append(node.right)
                    pq.append(node)        

            if (x_found and y_found):
                return x_parent != y_parent

            if x_found or y_found:
                return False

        return False
