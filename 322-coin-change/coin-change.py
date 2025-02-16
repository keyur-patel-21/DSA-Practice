class Solution:
    def coinChange(self, coins, amount):
        m = len(coins)
        n = amount
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]

        # Base case: if amount is 0, no coins are needed
        for i in range(m + 1):
            dp[i][0] = 0  

        for i in range(1, m + 1):
            for j in range(n + 1):
                if j < coins[i - 1]:  # If current coin value > amount
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coins[i - 1]])

        return -1 if dp[m][n] == float('inf') else dp[m][n]
