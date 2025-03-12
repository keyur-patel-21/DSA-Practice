class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        res = []
        nums.sort()

        for i in range(0, n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break 

            low = i + 1
            high = n - 1

            while low < high: 

                curSum = nums[i] + nums[low] + nums[high]

                if curSum == 0:
                    res.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while nums[low] == nums[low-1] and low < high:
                        low += 1
                    while nums[high] == nums[high+1] and low < high:
                        high -= 1
                elif curSum < 0:
                    low += 1
                else:
                    high -= 1

        return res
        