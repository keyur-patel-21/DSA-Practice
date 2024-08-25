class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = {}

        for i, n in enumerate(nums):
            if target-n in temp:
                return [i, temp[target-n]]
            else:
                temp[n] = i