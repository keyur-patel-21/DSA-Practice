class Solution(object):
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:  
            return len(nums) - 1

        l, r = 0, len(nums) - 1

        while l < r:  # Use l < r instead of l <= r
            mid = (l + r) // 2

            if nums[mid] < nums[mid + 1]:  
                # Peak must be on the right side
                l = mid + 1
            else:
                # Peak must be on the left side (or mid itself)
                r = mid  
        
        return l  # or return r (both will be the peak index)
