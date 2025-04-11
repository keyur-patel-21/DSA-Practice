class Solution(object):
    def findAnagrams(self, s, p):
        m = len(s)
        n = len(p)
        result = []

        freqMap = {}
        match = 0
        for ch in p:
            if ch in freqMap:
                freqMap[ch] += 1
            else:
                freqMap[ch] = 1
        
        for i in range(m):
            # in
            if s[i] in freqMap:
                freqMap[s[i]] -= 1
                if freqMap[s[i]] == 0:
                    match += 1

            if i >= n:
                if s[i-n] in freqMap:
                    freqMap[s[i-n]] += 1
                    if freqMap[s[i-n]] == 1:
                        match -= 1
        
            if match == len(freqMap):
                result.append(i-n+1)

        return result