class Solution(object):
    def deleteAndEarn(self, nums):
        
        if not nums:
            return None

        dp = [0] * (int(max(nums)) + 1)

        for num in nums:
            dp[num] += num

        if len(nums) == 1:
            return nums[0]

        for i in range(2, int(max(nums)) + 1):
            dp[i] = max(dp[i-1], (dp[i]+dp[i-2]))

        return dp[-1]
        