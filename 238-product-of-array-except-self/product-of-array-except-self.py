class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [None] * n
        rp = 1
        res[0] = rp

        # left pass
        for i in range(1, n):
            rp = rp * nums[i - 1]
            res[i] = rp

        rp = 1
        for i in range(n - 2, -1, -1):
            rp = rp * nums[i + 1]
            res[i] = res[i] * rp
        
        return res
        