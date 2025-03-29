class Solution(object):
    def subsets(self, nums):
        result = []

        def helper(pivot, path):

            # base
            result.append(path[:])

            # logic
            for i in range(pivot, len(nums)):
                path.append(nums[i])
                helper(i+1, path)
                path.pop()

        helper(0, [])
        return result
        