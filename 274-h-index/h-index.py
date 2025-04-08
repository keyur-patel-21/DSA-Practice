class Solution(object):
    def hIndex(self, citations):
        n = len(citations)

        arr = [0 for _ in range(n + 1)]

        for ele in citations:
            if ele >= n:
                arr[n] += 1
            else:
                arr[ele] += 1

        sum = 0

        for i in range(n, -1, -1):
            sum += arr[i]
            if sum >= i:
                return i

        return sum

        
        