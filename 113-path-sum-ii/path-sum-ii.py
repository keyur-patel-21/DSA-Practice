# Time Complexity (TC): O(N) 
# - We visit each node exactly once in a Depth-First Search (DFS) traversal.
# - Each node is processed in O(1) time, leading to an overall complexity of O(N), where N is the number of nodes in the tree.

# Space Complexity (SC): O(N)
# - In the worst case (a skewed tree), the recursion stack can go up to O(N).
# - Additionally, we store paths in the result list, which in the worst case could also be O(N) if all nodes contribute to valid paths.

# Approach:
# 1. We use DFS to traverse the binary tree, maintaining a running sum (curSum) and a list (curPath) to store the current path.
# 2. If we reach a leaf node and the path sum equals the targetSum, we add the path to the result list.
# 3. We recursively explore the left and right subtrees while updating the current sum and path.
# 4. After exploring a node, we backtrack by removing the last added value to restore the state before the recursive call.

class Solution(object):
    def pathSum(self, root, targetSum):
        res = []
        curSum = 0
        curPath = []

        def dfs(root, res, curSum, curPath, targetSum):
            if not root:
                return None

            curSum += root.val
            curPath.append(root.val)

            if not root.left and not root.right and curSum == targetSum:
                res.append(curPath[:])  # Append a shallow copy of the current path

            dfs(root.left, res, curSum, curPath, targetSum)
            dfs(root.right, res, curSum, curPath, targetSum)

            # Backtracking step: Remove the last node from the path and subtract its value
            curSum -= root.val
            curPath.pop()

        dfs(root, res, curSum, curPath, targetSum)
        return res
