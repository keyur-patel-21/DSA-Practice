class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m =len(board)
        n = len(board[0])
        dirs = [[0,1], [1,0], [-1,0], [0,-1]]

        def helper(i, j, idx):
            # base
            if idx == len(word):
                return True
            
            if not (0<=i<m and 0<=j<n and board[i][j] == word[idx]):
                return False

            # logic
            
            board[i][j] = "#"
            for dire in dirs:
                r = i + dire[0]
                c = j + dire[1]
                if helper(r, c, idx+1):
                    return True
            board[i][j] = word[idx]
            return False

        for i in range(m):
            for j in range(n):
                if helper(i,j,0):
                    return True
        
        return False