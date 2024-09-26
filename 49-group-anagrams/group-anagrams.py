class Solution(object):
    def groupAnagrams(self, strs):
        res = defaultdict(list)

        for s in strs:
            char = [0] * 26

            for c in s:
                char[ord(c) - ord("a")] += 1

            res[tuple(char)].append(s)
        
        return res.values()