class Solution(object):
    def combinationSum(self, candidates, target):
        result = []

        def helper(candidates, p, target, path):
            # base
            if target < 0 or p == len(candidates):
                return

            if target == 0:
                result.append(path[:])
                return 

            # for loop
            for i in range(p, len(candidates)):
                path.append(candidates[i])
                helper(candidates, i, target-candidates[i], path)
                path.pop()

        helper(candidates, 0, target, [])
        return result