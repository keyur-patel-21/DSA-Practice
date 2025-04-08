class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n  # Make sure k is within bounds
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)


    def reverse(self, nums, l, r):
        while l < r:
            self.swap(nums, l, r)
            l += 1
            r -= 1
    
    def swap(self, nums, l, r):
        nums[l], nums[r] = nums[r], nums[l]

        