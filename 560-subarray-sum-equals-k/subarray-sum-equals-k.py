class Solution(object):
    def subarraySum(self, nums, k):
        
        
        myDict = {}
        
        rSum = 0
        res = 0

        myDict[0] = 1

        for i in range(len(nums)):
            rSum += nums[i]

            ele = rSum - k

            if ele in myDict:
                res += myDict[ele]
            
            if rSum in myDict:
                myDict[rSum] += 1
            else:
                myDict[rSum] = 1

        return res 



        