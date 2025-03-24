class Solution(object):
    def orangesRotting(self, grid):
        q = collections.deque()
        time = 0
        fresh = 0
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]         

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return time

        while q:
            level = len(q)
            for i in range(level):
                cur = q.popleft()
                for dire in dirs:
                    nr = cur[0] + dire[0]
                    nc = cur[1] + dire[1]
                    if 0 <= nr <len(grid) and 0 <= nc <len(grid[0]):
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            q.append((nr, nc))
                            fresh -= 1

            time += 1

        
        if fresh != 0:
            return -1

        return time -1 
