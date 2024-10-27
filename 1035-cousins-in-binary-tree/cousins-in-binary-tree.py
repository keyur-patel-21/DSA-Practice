# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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