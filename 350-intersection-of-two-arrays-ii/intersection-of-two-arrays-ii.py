class Solution(object):
    def intersect(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)

        if n1 > n2:
            return self.intersect(nums2, nums1)

        freqMap = {}

        for ele in nums1:
            if ele in freqMap:
                freqMap[ele] += 1
            else:
                freqMap[ele] = 1

        result = []

        for ele in nums2:
            if ele in freqMap and freqMap[ele] > 0:
                freqMap[ele] -= 1
                result.append(ele)

        return result
        