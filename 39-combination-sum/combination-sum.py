class Solution(object):
    def combinationSum(self, candidates, target):
        result = []

        def helper(candidates, i, target, result, path):
            # base
            if target == 0:
                result.append(path[:])
                return  

            if target < 0 or i == len(candidates):
                return

            # logic

            # No choose
            helper(candidates, i+1, target, result, path)

            # choose
            path.append(candidates[i])
            helper(candidates, i, target-candidates[i], result, path)
            path.pop()
        
        helper(candidates, 0, target, result, [])

        return result