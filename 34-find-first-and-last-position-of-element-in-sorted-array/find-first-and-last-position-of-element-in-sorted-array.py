class Solution(object):
    def searchRange(self, nums, target):
        
        first = self.binarySearch(nums, target, True)
        last = self.binarySearch(nums, target, False)
    
        return [first, last]
        
    def binarySearch(self, nums, target, isFirst):

        l, r = 0, len(nums)-1
        ans = - 1

        while (l <= r ):
            m = (l + r) // 2

            if target == nums[m]:
                ans = m
                if isFirst:
                    r = m - 1
                else:
                    l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1

        return ans
