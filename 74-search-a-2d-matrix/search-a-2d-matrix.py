class Solution(object):
    def searchMatrix(self, matrix, target):
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break

            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                return False

        l, r = 0, len(matrix[mid]) - 1

        while l <= r:
            
            m = (l + r) // 2

            if matrix[mid][m] == target:
                return True

            if target < matrix[mid][m]:
                r = m - 1
            else:
                l = m + 1

        return False
            
        