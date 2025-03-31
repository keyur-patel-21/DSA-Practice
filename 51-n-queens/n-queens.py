class Solution(object):
    def solveNQueens(self, n):
        result  = []
        matrix = [[None for _ in range(n)] for _ in range(n)]

        def helper(i):
            # base
            if i == n:
                path = []
                for r in matrix:
                    rowString = ""
                    for c in r:
                        if c:
                            rowString += "Q"
                        else:
                            rowString += "."
                    path.append(rowString)
                result.append(path)
                return


            # logic
            for j in range(n):
                if isSafe(i, j):
                    matrix[i][j] = True
                    helper(i+1)
                    matrix[i][j] = None

        def isSafe(i, j):
            r, c = i, j

            while r>=0:
                if matrix[r][c]:
                    return False
                r -= 1
            r, c = i, j

            while r>=0 and c>=0:
                if matrix[r][c]:
                    return False
                r -= 1
                c -= 1
            r, c = i, j

            while r>=0 and c<n:
                if matrix[r][c]:
                    return False
                r -= 1
                c += 1
            
            return True


        helper(0)
        return result

        