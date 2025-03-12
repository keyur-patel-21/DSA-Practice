class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        res = []

        target = 0

        for i in range(0, n-2):
            if (i > 0 and nums[i] == nums[i -1]):  #condition to skip the same element
                continue
            if (nums[i] > 0):   #as we have sorted the array, we cant form a negative sum from other two elements  
                break           # if first element is positive

            low = i +1
            high = n - 1

            while low < high:
                curSum = nums[i] + nums[low] + nums[high]

                if curSum == target:
                    res.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while (low < high and nums[low] == nums[low-1]):
                        low += 1
                    while (low < high and nums[high] == nums[high+1]):
                        high -= 1
                elif curSum < target:
                    low += 1
                else:
                    high -= 1
            
        return res