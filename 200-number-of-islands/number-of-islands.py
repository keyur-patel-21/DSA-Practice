class Solution(object):
    def numIslands(self, grid):
        q = collections.deque()
        count = 0
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    q.append((i, j))
                    grid[i][j] = '0'
                    while q:
                        # for i in range(len(q)):
                            cur = q.popleft()
                            for dire in dirs:
                                nr = cur[0] + dire[0]
                                nc = cur[1] + dire[1]
                                if 0<=nr<len(grid) and 0<=nc<len(grid[0]):
                                    if grid[nr][nc] == '1':
                                        grid[nr][nc] = '0'
                                        q.append((nr, nc))
        
        return count