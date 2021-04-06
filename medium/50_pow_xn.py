class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res = 1.0
        if n < 0 :
            x = 1/x
            n = -1 * n
        while(n):
            if n & 1 : #if n is odd:
                res *= x
            x = x * x 
            n = n >> 1 
        print(res)