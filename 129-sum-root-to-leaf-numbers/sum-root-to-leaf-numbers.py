
class Solution(object):
    def sumNumbers(self, root):
        def sum(root, digit):
            if not root:
                return 0

            digit = digit * 10 + root.val
            if not root.left and not root.right:
                return digit
            return sum(root.left, digit) + sum(root.right, digit)

        return sum(root, 0)