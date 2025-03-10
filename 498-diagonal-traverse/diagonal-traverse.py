class Solution(object):
    def findDiagonalOrder(self, mat):
        m = len(mat)
        n = len(mat[0])

        res = [None] * (m*n)
        r, c = 0, 0
        upward = True

        for i in range(0, m*n):
            res[i] = mat[r][c]

            if upward:
                if c == n-1:
                    r += 1
                    upward = False
                elif r == 0:
                    c += 1
                    upward = False
                else:
                    r -= 1
                    c += 1
            else:
                if r == m - 1:
                    c += 1
                    upward = True
                elif c == 0:
                    r += 1
                    upward = True
                else:
                    r += 1
                    c -= 1


        return res