class Solution(object):
    def findMaxLength(self, nums):
        
        if (not nums) or (len(nums) == 0) or (len(nums) == 1):
            return 0

        dict = {}
        dict[0] = -1

        rSum = 0
        res = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                rSum -= 1
            else:
                rSum += 1

            if rSum in dict:
                res = max(res, (i - dict[rSum]))
            else:
                dict[rSum] = i
        
        return res
