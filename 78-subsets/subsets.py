class Solution(object):
    def subsets(self, nums):
        result = [[]]  # Start with an empty subset

        for num in nums:  # Iterate through each number
            new_subsets = [subset + [num] for subset in result]  # Create new subsets
            result.extend(new_subsets)  # Add them to the result

        return result
