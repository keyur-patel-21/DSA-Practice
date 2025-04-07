class Solution(object):
    def findClosestElements(self, arr, k, x):
        l, r = 0, len(arr)-k

        while l < r:
            m = (l + r) // 2
            distL = (x - arr[m])
            distR = (arr[m + k] - x)

            if distL > distR:
                l = m + 1
            else:
                r = m

        return arr[l:l+k]
        