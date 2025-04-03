class Solution(object):
    def lengthOfLongestSubstring(self, s):
        slow = 0
        memory = set()
        length = 0

        for i in range(len(s)):
            if s[i] in memory:
                while s[slow] != s[i]:
                    memory.remove(s[slow])
                    slow += 1
                slow += 1

            memory.add(s[i]) 
            length = max(length, (i-slow+1))

        return length
