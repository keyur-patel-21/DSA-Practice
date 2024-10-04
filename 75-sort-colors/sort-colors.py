class Solution(object):
    def sortColors(self, nums):
       l, m = 0, 0
       r = len(nums) - 1

       def swap(a, b):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] =temp

       while m <= r:
        if nums[m] == 0:
            swap(m, l)
            l += 1
            m += 1
        elif nums[m] == 1:
            m += 1
        else:
            swap(m, r)
            r -= 1
