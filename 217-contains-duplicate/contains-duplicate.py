class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp = set()

        for num in nums:
            if num in temp:
                return True
            else:
                temp.add(num)
            
        return False
        