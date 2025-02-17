class Solution(object):
    def deleteAndEarn(self, nums):

        if not nums:
            return 0

        maximum = max(nums)
        dp = [0] * (maximum+1) 

        for num in nums:
            dp[num] += num

        if maximum == 1:
            return dp[1] 
        
        for i in range(2, maximum+1):
            dp[i] = max(dp[i-1], dp[i] + dp [i-2])

        return dp[maximum]