class Solution(object):
    def lengthOfLongestSubstring(self, s):
        slow = 0
        memory = {}
        length = 0

        for i in range(len(s)):
            if s[i] in memory:
                slow = max(slow, memory[s[i]]+1)

            memory[s[i]] = i 
            length = max(length, (i-slow+1))

        return length
