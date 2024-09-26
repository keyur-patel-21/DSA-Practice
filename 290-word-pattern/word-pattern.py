class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split(" ")
        mapPS, mapSP = {}, {}

        for i in range(len(pattern)):

            c1, c2 = pattern[i], s[i]

            if((c1 in mapPS and mapPS[c1] != c2) or 
                (c2 in mapSP and mapSP[c2] != c1) or
                len(pattern) != len(s)):
                return False

            mapPS[c1] = c2
            mapSP[c2] = c1
        
        return True