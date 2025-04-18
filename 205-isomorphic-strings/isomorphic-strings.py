class Solution(object):
    def isIsomorphic(self, s, t):
        mapST = {}
        mapTS = {}

        if len(s) != len(t):
            return False

        for ch1, ch2 in zip(s, t):
            if (ch1 in mapST and mapST[ch1] != ch2) or (ch2 in mapTS and mapTS[ch2] != ch1) :
                return False

            mapST[ch1] = ch2
            mapTS[ch2] = ch1
        
        return True

        