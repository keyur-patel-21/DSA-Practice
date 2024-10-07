class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = len(matrix) 
        cols = len(matrix[0]) 

        r, c = rows - 1, 0

        while(r >= 0 and c < cols):
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                c += 1
            else:
                r -= 1
            
        return False
        