class Solution(object):
    def searchMatrix(self, matrix, target):
        no_of_rows, no_of_cols = len(matrix), len(matrix[0])

        top, bottom = 0, no_of_rows - 1

        while top <= bottom:
            mid_row = (top+bottom) // 2

            if target < matrix[mid_row][0]:
                bottom = mid_row - 1
            elif target > matrix[mid_row][-1]:
                top = mid_row + 1
            else:
                break
        
        if not (top <= bottom):
            return False

        row = (top+bottom) // 2
        l, r = 0, no_of_cols - 1

        while l <= r:
            mid = (l + r) // 2

            if target == matrix[row][mid]:
                return True
            elif target <= matrix[row][mid]:
                r = mid - 1
            else:
                l = mid + 1 
        return False
        