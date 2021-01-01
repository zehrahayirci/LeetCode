class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        s = str(abs(x))
        s = s[::-1]
        i = int(s)
        if i < -2147483648 or i > 2147483648:
            return 0
        elif x < 0:
            return(-1*i)
        else:
            return(i)
        