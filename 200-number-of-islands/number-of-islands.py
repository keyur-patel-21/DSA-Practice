class Solution(object):
    def numIslands(self, grid):
        island = 0
        m = len(grid)
        n = len(grid[0])

        dirs = [[0,1], [1,0], [0,-1], [-1,0]]

        def dfs(grid, i ,j):
            #base
            if not(0<=i<m and 0<=j<n):
                return
            if grid[i][j] != "1":
                return

            # logic
            grid[i][j] = "0"
            for dire in dirs:
                r = i + dire[0]
                c = j + dire[1]
                dfs(grid, r, c)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    island += 1
                    dfs(grid, i , j)
                    

        return island