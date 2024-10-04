class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            l, r = i + 1, len(nums) - 1
            while l < r:
                answer = n + nums[l] + nums[r]
                if answer > 0:
                    r -= 1
                elif answer < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res 
        