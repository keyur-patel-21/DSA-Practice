class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1 = {}
        dict2 = {}

        for ch in s:
            if ch in dict1:
                dict1[ch] += 1
            else:
                dict1[ch] = 1
        
        for ch in t:
            if ch in dict2:
                dict2[ch] += 1
            else:
                dict2[ch] = 1

        if dict1 == dict2:
            return True
        else:
            return False