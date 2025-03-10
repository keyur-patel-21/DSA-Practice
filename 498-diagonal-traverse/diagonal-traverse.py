class Solution(object):
    def findDiagonalOrder(self, mat):
        m, n = len(mat), len(mat[0])
        r, c = 0, 0

        res = [None] * (m*n)
        upDir = True

        for i in range(0, m*n):
            res[i] = mat[r][c]

            if upDir:
                if c == n - 1:
                    r += 1
                    upDir = False
                elif r == 0:
                    c += 1
                    upDir = False
                else:
                    r -= 1
                    c += 1
            else:
                if r == m - 1:
                    c += 1
                    upDir = True
                elif c == 0:
                    r += 1
                    upDir = True
                else:
                    r += 1
                    c -= 1

        return res
        