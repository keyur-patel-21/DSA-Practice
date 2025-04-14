class Solution(object):
    def findMin(self, nums):
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] <= nums[r]:
                return nums[l]

            m = (l+r) // 2

            if nums[m-1] > nums[m] < nums[m+1]:
                return nums[m]

            if nums[l] <= nums[m] and nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
            