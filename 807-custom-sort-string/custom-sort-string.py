class Solution(object):
    def customSortString(self, order, s):
        freqMap = {}
        result = []

        for c in s:
            if c in freqMap:
                freqMap[c] += 1
            else:
                freqMap[c] = 1

        for c in order:
            if c in freqMap:
                result.append(c * freqMap[c])
                freqMap.pop(c)

        
        for c in freqMap:
            result.append(c * freqMap[c])

        return "".join(result)

        
        
        