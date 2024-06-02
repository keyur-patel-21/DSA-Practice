class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = len(arr)
        if n == 0:
            return []

        # Initialize result array with the same length as arr
        result = [-1] * n

        # The last element is always -1
        max_right = -1
        
        # Traverse the array from right to left
        for i in range(n - 1, -1, -1):
            result[i] = max_right
            if arr[i] > max_right:
                max_right = arr[i]

        return result
