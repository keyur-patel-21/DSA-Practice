class Solution(object):
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])

        r, c = m - 1, 0

        while(r >= 0 and c < n):
            if (matrix[r][c] == target):
                return True
            elif (matrix[r][c] > target):
                r -= 1
            else:
                c += 1
        
        return False
            

        
