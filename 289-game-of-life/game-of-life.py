class Solution(object):
    def gameOfLife(self, board):
        
        m = len(board)
        n = len(board[0])
        
        dirs = [[0,1] ,[1,0], [0,-1], [-1,0], [1,1], [-1,-1], [-1,1], [1,-1]]

        for i in range(m):
            for j in range(n):

                count = self.countAlive(i, j, board, dirs, m, n)

                if(board[i][j] == 1):
                    if(count < 2 or count > 3):
                        board[i][j] = 2
                elif(board[i][j] == 0):
                    if(count == 3):
                        board[i][j] = 3

                        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0 
                elif board[i][j] == 3:
                    board[i][j] = 1


    def countAlive(self, i, j, board, dirs, m, n):

        count = 0

        for dir in dirs:
            r = i + dir[0]
            c = j + dir[1]

            if 0 <= r < m and 0 <= c < n:
                if (board[r][c] == 1 or board[r][c] == 2):
                    count += 1

        return count


