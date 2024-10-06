class Solution(object):
    def spiralOrder(self, matrix):
        res = []
        left, right = 0 , len(matrix[0])
        top, bottom = 0 , len(matrix)

        while top < bottom  and left < right:

            # Moving right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # Moving down
            for i in range(top, bottom):
                res.append(matrix[i][right- 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            # movign left
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # moving up
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res