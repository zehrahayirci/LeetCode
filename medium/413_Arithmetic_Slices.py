class Solution(object):
   def numberOfArithmeticSlices(self, A):
       """
       :type A: List[int]
       :rtype: int
       """
       n =len(A)
       if n < 3:
           return 0
       else:
           r = 0
           for i in range(n):
               j =i+3
               
               #print(i,j)
               #print(r,A[i:j])
               while(j<=n and self.checkArim(A[i:j])):
                   r+=1
                   j+=1
                   print(r,A[i:j])
       return r
   
   def checkArim(self,A_s):
       #print("checkarim",A_s)
       if len(A_s) < 3:
           return False
       diff = A_s[1] - A_s[0]
       #print("diff",diff)
       for i in range(2,len(A_s)):
           print(A_s[i],A_s[i-1])
           if(A_s[i]-A_s[i-1]) != diff:
               #print("f",A_s[i]-A_s[i-1],diff)
               return False
       return True