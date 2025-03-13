class Solution(object):
    def removeDuplicates(self, nums):
        fast, slow = 0, 0
        count = 0

        while fast < len(nums):
            if fast > 0 and nums[fast] == nums[fast - 1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow

            
        