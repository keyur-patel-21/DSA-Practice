class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        
        if n < 0:
            x = 1.0 / x
            n = -n

        result = self.myPow(x, n // 2)

        if n % 2 == 0:
            return result * result
        else:
            return result * result * x
