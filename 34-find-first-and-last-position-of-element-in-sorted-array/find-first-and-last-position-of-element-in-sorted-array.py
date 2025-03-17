# Time Complexity (TC): O(log N) 
# - The binary search is performed twice: once to find the first occurrence and once to find the last occurrence. 
# - Each binary search runs in O(log N) time, so the overall complexity is O(2 * log N) = O(log N).

# Space Complexity (SC): O(1)
# - The solution only uses a few extra variables and does not require any additional data structures, leading to O(1) space usage.

# Approach:
# - Use binary search twice to efficiently find the first and last occurrence of the target in a sorted array.
# - First binary search (`isFirst=True`) looks for the first occurrence by adjusting `r = m - 1` when a match is found.
# - Second binary search (`isFirst=False`) looks for the last occurrence by adjusting `l = m + 1` when a match is found.
# - If the target is not found, return [-1, -1].

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
