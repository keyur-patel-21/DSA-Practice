class Solution(object):
    def combinationSum(self, candidates, target):
        result = []

        def helper(candidates, target, i, path):

            # base
            if target == 0:
                result.append(path[:])
                return 
            
            if target < 0 or i == len(candidates):
                return

            # no choose
            helper(candidates, target, i+1, path)

            # choose
            path.append(candidates[i])
            helper(candidates, target-candidates[i], i, path)
            path.pop()

        
        helper(candidates, target, 0, [])
        return result