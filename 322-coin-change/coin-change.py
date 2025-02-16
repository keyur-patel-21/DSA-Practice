class Solution(object):
    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount+1)

        dp[0] = 0

        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] = min(dp[j], 1 + dp[j-coin])

        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[amount]
        