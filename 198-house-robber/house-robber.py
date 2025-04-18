class Solution(object):
    def rob(self, nums):
        rob0, rob1 = 0, 0 

        for house in nums:
            temp = max(rob0 + house, rob1)
            rob0 = rob1
            rob1 = temp

        return rob1
        
        