# Approach:
# - This function finds the minimum element in a rotated sorted array.
# - The idea is to use a modified binary search.
# - If the array is already sorted (nums[l] <= nums[r]), return nums[l].
# - Otherwise, find the middle element and check if it is the minimum.
# - If nums[mid] is smaller than both its left and right neighbors, return nums[mid].
# - If nums[mid] is in the sorted right half, move left (r = mid - 1).
# - Otherwise, move right (l = mid + 1).
#
# Time Complexity (TC): O(log N) → Since we are using binary search.
# Space Complexity (SC): O(1) → No extra space is used apart from variables.

class Solution(object):
    def findMin(self, nums):
        if len(nums) == None or len(nums) == 0:
            return -1

        l, r = 0, len(nums) - 1

        while l <= r:
            
            if nums[l] <= nums[r]:
                return nums[l]

            mid = (l + r) // 2

            if ((mid >= 0 and nums[mid] <= nums[mid-1]) and (mid <= len(nums)-2 or nums[mid] <= nums[mid+1])):
                return nums[mid]
            elif nums[mid] <= nums[r]:
                r = mid - 1
            else:
                l = mid + 1
