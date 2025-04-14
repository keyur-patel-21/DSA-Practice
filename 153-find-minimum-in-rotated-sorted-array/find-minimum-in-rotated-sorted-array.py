class Solution(object):
    def findMin(self, nums):
        l, r = 0, len(nums)-1
        if nums == None or len(nums) == 0:
            return None

        while l<=r:
            if nums[l] <= nums[r]:
                return nums[l]
            m = (l+r) // 2

            if nums[m-1] > nums[m] < nums[m+1]:
                return nums[m]
            if nums[l] <= nums[m] and nums[m] > nums[r]:   #we are in left
                
                l = m + 1
            else:   #we are in right
                r = m - 1
