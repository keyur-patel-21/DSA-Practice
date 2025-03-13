class Solution(object):
    def removeDuplicates(self, nums):
        slow, fast = 0, 0
        count = 0
        k = 2

        while fast <= len(nums)-1:
            if fast > 0 and nums[fast] == nums[fast - 1]: 
                count += 1
            else:
                count = 1

            if count <= k:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow


        