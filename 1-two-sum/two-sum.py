class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = {}

        for i, num in enumerate(nums):
            if target-num in temp:
                return[i, temp[target-num]]
            else:
                temp[num] = i 