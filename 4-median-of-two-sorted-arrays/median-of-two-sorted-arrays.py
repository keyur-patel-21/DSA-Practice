class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        n1 = len(nums1)
        n2 = len(nums2)

        l, r = 0, n1

        while l <= r:
            x1 = (l + r) // 2
            x2 = (n1 + n2 + 1) // 2 - x1

            l1 = float("-inf") if x1 == 0 else nums1[x1 - 1]
            r1 = float("inf") if x1 == n1 else nums1[x1]
            l2 = float("-inf") if x2 == 0 else nums2[x2 - 1]
            r2 = float("inf") if x2 == n2 else nums2[x2]

            if l1 <= r2 and l2 <= r1:
                if (n1 + n2) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                else:
                    return max(l1, l2)
            elif l1 > r2:
                r = x1 - 1
            else:
                l = x1 + 1
