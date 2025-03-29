class Solution(object):
    def subsets(self, nums):
        result = []

        def helper(i, path, nums):
            # base
            if i == len(nums):
                result.append(path[:])
                return



            # No choose
            helper(i+1, path, nums)


            # choose
            path.append(nums[i])
            helper(i+1, path, nums)
            path.pop()

        helper(0, [], nums)
        return result