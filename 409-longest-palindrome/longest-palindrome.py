class Solution(object):
    def longestPalindrome(self, s):
        seen = set()
        res = 0
        for c in s:
            if c in seen:
                seen.remove(c)
                res += 2
            else:
                seen.add(c)

        if seen:
            res += 1

        return res
        