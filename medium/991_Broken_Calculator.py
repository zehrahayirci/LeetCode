class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        c = 0 
        while (Y > X):
            if Y %2 == 0:
                Y = Y / 2 
                c+=1
            else:
                Y = Y +1
                c+=1
        if Y == X:
            return c
        else:
            return c + (X-Y)