class Solution(object):
    def findPeakElement(self, nums):
        if nums == None and len(nums) == 0:
            return None
        
        if len(nums) == 1:
            return 0
        
        if nums[0]>nums[1]:
            return 0
        
        if nums[-1]>nums[-2]:
            return len(nums)-1

        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) // 2

            if nums[m-1] < nums[m] > nums[m+1]:
                return m
            else:
                if nums[m-1] >= nums[m+1]:
                    r = m - 1
                else:
                    l = m + 1