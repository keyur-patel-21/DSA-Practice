class Solution(object):
    def strStr(self, haystack, needle):
        n = len(haystack)
        m = len(needle)

        i, j = 0, m

        while j <= n:
            part = haystack[i:j]
            if part == needle:
                return i
            else:
                i += 1
                j += 1


        return -1
        