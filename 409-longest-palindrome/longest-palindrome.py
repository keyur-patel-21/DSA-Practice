class Solution(object):
    def longestPalindrome(self, s):
        
        seen = set()
        result = 0

        for c in s:
            if c in seen:
                seen.remove(c)
                result += 2
            else:
                seen.add(c)

        if not seen:
            return result
        else:
            result += 1
            return result