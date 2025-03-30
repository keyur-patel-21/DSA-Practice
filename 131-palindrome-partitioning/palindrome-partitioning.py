class Solution(object):
    def partition(self, s):
        
        res = []

        def helper(pivot, path):

            # base
            if pivot == len(s):
                res.append(path[:]) 


            # logic
            for i in range(pivot, len(s)):
                subString = s[pivot:i+1]
                if isPalindrome(subString):
                    path.append(subString)
                    helper(i+1, path)
                    path.pop()

            
        def isPalindrome(subString):
            return subString == subString[::-1]

        helper(0, [])
        
        return res

        