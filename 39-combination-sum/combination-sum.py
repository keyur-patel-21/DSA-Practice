class Solution(object):
    def combinationSum(self, candidates, target):
        result = []

        def helper(i, path, target):
            # base
            if target == 0:
                result.append(path[:])
                return

            if target < 0 or i == len(candidates):
                return 


            # no choose
            helper(i+1, path, target)

            # choose:
            path.append(candidates[i])
            helper(i, path, target-candidates[i])
            path.pop()

        helper(0, [], target)
        return result
        