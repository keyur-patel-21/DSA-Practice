class Solution(object):
    def findMin(self, nums):
        if len(nums) == None or len(nums) == 0:
            return -1

        l, r = 0, len(nums) - 1

        while l <= r:
            
            if nums[l] <= nums[r]:
                return nums[l]

            mid = (l + r) // 2

            if ((mid == 0 or nums[mid] <= nums[mid-1]) and (mid == len(nums)-1 or nums[mid] <= nums[mid+1]) ):
                return nums[mid]
            elif nums[mid] <= nums[r]:
                r = mid - 1
            else:
                l = mid + 1
        

        