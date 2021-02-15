class Solution:
    def numberOfSteps (self, num: int) -> int:
        co=0
        while(num):
            
            if num%2==0:
                co+=1
                num=num/2
            else:
                co+=1
                num-=1
        return co