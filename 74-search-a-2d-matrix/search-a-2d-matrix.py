class Solution(object):
    def searchMatrix(self, matrix, target):
        rows, cols = len(matrix), len(matrix[0])

        top, bottom = 0, rows - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][cols - 1]:
                top = mid + 1
            else:
                midrow = mid  # This is the correct row where target might exist
                break
        else:
            return False  # If we exit the loop, the target is not in any row range

        l, r = 0, cols - 1

        while l <= r:
            m = (l + r) // 2

            if matrix[midrow][m] == target:
                return True
            elif target < matrix[midrow][m]:
                r = m - 1
            else:
                l = m + 1
            
        return False