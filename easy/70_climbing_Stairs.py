class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        
        if n== 1:
            return 1
        if n==2:
            return 2
        
        one=2
        two=1
        for i in range(2,n):
            a = one+two
            two=one
            one=a
        return a
        #else:
        #    return (self.climbStairs(n-1)+self.climbStairs(n-2))
        