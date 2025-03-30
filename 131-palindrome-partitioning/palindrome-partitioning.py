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
            l, r = 0, len(subString)-1

            while l<=r:
                if subString[l] != subString[r]:
                    return False
                l += 1
                r -= 1

            return True

        helper(0, [])
        
        return res

        