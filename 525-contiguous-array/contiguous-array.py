class Solution(object):
    def findMaxLength(self, nums):

        if ((not nums) or (len(nums) == 0) or (len(nums) == 1)):
            return 0
        
        myDict = {}

        res = 0
        rSum = 0

        myDict[0] = -1
        
        for i in range(len(nums)):

            if nums[i] == 0:
                rSum -= 1
            else:
                rSum += 1

            if rSum in myDict:
                res = max(res, (i - myDict[rSum])) 
            else:
                myDict[rSum] = i    


        return res   