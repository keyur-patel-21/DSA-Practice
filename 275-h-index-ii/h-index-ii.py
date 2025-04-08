class Solution(object):
    def hIndex(self, citations):
        n = len(citations)

        l , r = 0, n-1

        while l <= r:
            m = (l + r) // 2

            diff = n - m

            if diff == citations[m]: return diff

            if citations[m] > diff:
                r = m - 1
            else:
                l = m + 1 
        
        return n - l
        