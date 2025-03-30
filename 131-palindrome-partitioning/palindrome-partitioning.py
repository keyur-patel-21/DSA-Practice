class Solution(object):
    def partition(self, s):
        
        res = []

        def helper(pivot, i, sum, path):

            #base case
            if i == len(s):
                if sum==len(s):
                    res.append(path[:])
                return


            # logic

            # No choose
            helper(pivot, i+1, sum, path)

            # choose
            sub = s[pivot:i+1]
            if isPalindrome(sub):
                path.append(sub)
                helper(i+1, i+1, sum+len(sub), path)
                path.pop()


            
        def isPalindrome(subString):
            l, r = 0, len(subString)-1

            while l<=r:
                if subString[l] != subString[r]:
                    return False
                l += 1
                r -= 1

            return True

        helper(0, 0, 0, [])
        
        return res

        