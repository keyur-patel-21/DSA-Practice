class Solution(object):
    def groupAnagrams(self, strs):
        memory = {}

        for word in strs:
            value = [0] * 26
            for ch in word:
                value[ord(ch) - ord("a")] += 1

            key = tuple(value)

            if key in memory:
                memory[key].append(word)
            else:
                memory[key] = [word]

        return memory.values()

        