class Solution(object):
    def rob(self, nums):
        
        # base case
        if len(nums) == 1:
            return nums[0]

        nums[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            nums[i] = max(nums[i-1], nums[i]+nums[i-2])

        return nums[len(nums) - 1]
        