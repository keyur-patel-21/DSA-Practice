class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        input = s.strip()
        arr = input.split(" ")
        
        return len(arr[-1])
        