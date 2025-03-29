class Solution(object):
    def combinationSum(self, candidates, target):
        result = []

        def helper(target, pivot, path):
            # base
            if target == 0:
                result.append(path[:])
                return
            
            if target < 0 or pivot == len(candidates):
                return

            # logic:
            for i in range(pivot, len(candidates)):
                path.append(candidates[i])
                helper(target-candidates[i], i, path)
                path.pop()        
        
        helper(target, 0, [])
        return result