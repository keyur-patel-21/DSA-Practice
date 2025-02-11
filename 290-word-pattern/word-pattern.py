class Solution(object):
    def wordPattern(self, pattern, s):
        
        s = s.split()
        if len(s) != len(pattern):
            return False
        mapPS, mapSP = {}, {}

        for i in range(len(pattern)):
            c1, s1 = pattern[i], s[i]

            if((c1 in mapPS and mapPS[c1] != s1) or (s1 in mapSP and mapSP[s1] != c1)):
                return False

            mapPS[c1] = s1
            mapSP[s1] = c1

        return True        