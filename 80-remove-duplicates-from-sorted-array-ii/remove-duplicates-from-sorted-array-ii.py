class Solution(object):
    def removeDuplicates(self, nums):
        slow, fast = 0, 0
        n = len(nums)
        k = 2

        while (fast < n):
            if (nums[fast] == nums[fast - 1] and fast > 0):
                count += 1
            else:
                count = 1

            if count <= k:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow
        