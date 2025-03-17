# Time Complexity: O(log N) - We use a binary search approach, reducing the search space by half in each iteration.
# Space Complexity: O(1) - We use a constant amount of extra space.
# 
# Approach:
# - If the array has only one element, return its index (0).
# - Check if the first or last element is a peak, return their index if true.
# - Use binary search to find a peak element:
#   - If the middle element is greater than its neighbors, return its index.
#   - If the left neighbor is greater, move left (`r = m - 1`).
#   - Otherwise, move right (`l = m + 1`).
# - The algorithm ensures finding a peak in logarithmic time.


class Solution(object):
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0

        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
                return m
            elif nums[m-1] > nums[m]:
                r = m - 1
            else:
                l = m + 1
        