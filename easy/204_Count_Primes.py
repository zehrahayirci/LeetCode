import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        is_prime =[False,False]+[True]*(n-1)
        count=0
        for i in range(2,n):
            if is_prime[i]:
                count+=1
                for j in range(i, n , i):
                    is_prime[j] = False
        return count
            
    
    
    def isPrime(self,n):
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                return False
        return True
    def countPrimesClassic(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        count =0
        for i in range(2,n):
            if self.isPrime(i):
                count+=1
        return count
            
            
            
        