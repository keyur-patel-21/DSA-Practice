class Solution(object):
    def searchRange(self, nums, target):
        
        first = self.binarySearch(nums, target, True)
        last = self.binarySearch(nums, target, False)

        return [first, last]
    def binarySearch(self, nums, target, isFirst):

        l, r = 0, len(nums) - 1
        ans = -1
        
        while  l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                ans = mid
                if isFirst:
                    r = mid - 1
                else:
                    l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        return ans
