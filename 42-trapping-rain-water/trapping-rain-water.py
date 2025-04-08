class Solution(object):
    def trap(self, height):
        l, r = 0, len(height) - 1
        lw, rw = height[l], height[r]
        result = 0

        while l <= r:
            if rw > lw:
                if height[l] < lw:
                    result += abs(height[l]-lw)
                else:
                    lw = height[l]
                l += 1                    
            else:
                if height[r] < rw:
                    result += abs(height[r]-rw)
                else:
                    rw = height[r]
                r -= 1
        return result
        