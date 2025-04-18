class Solution(object):
    def isIsomorphic(self, s, t):
        mapST = {}
        mapTS = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            ch1 = s[i]
            ch2 = t[i]

            if (ch1 in mapST and mapST[ch1] != ch2) or (ch2 in mapTS and mapTS[ch2] != ch1) :
                return False

            mapST[ch1] = ch2
            mapTS[ch2] = ch1
        
        return True

        