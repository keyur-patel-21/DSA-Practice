class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = ""
        for ch in s:
            if ch.isalnum():
                temp += ch.lower()
        
        return temp == temp[::-1]