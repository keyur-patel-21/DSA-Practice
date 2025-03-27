class Solution(object):
    def updateMatrix(self, mat):
        m = len(mat)
        n = len(mat[0])

        q = collections.deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                elif mat[i][j] == 1:
                    mat[i][j] = -1

        dirs = [[1,0], [0,1], [0,-1], [-1,0]]

        distance = 1
        
        while q:
            level = len(q)
            for i in range(level):
                cur = q.popleft()
                for dire in dirs:
                    r = cur[0] + dire[0]
                    c = cur[1] + dire[1]

                    if 0<=r<m and 0<=c<n:
                        if mat[r][c] == -1:
                            mat[r][c] = distance
                            q.append((r, c))

            distance += 1
        
        return mat


        