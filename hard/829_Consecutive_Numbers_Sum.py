class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 1
        c=0
        for j in range(1,N/2+2):
            i = j * 1.0
            #print(i,N/i)
            if ((N/i)-floor(N / i) == 0.5) and (floor(N / i) - (i/2)) >=0 and j%2==0:
                #print("bir")
                c+=1
            elif abs(floor(N/i)-(N / i))<0.00005 and floor(N / i) - (i-1)/2 >=1 and j%2==1:
                #print("iki")
                c+=1
        return c
        