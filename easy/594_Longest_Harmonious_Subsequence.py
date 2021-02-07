from collections import Counter 
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1 or len(nums)==0:
            return 0
            
        cnt = Counter(nums).items()
        cnt= sorted(cnt,key=lambda x:x[0])
        maxx=0
        if(len(cnt))==1:
            return 0
        for i in range(len(cnt)-1):
            if abs(cnt[i][0] - cnt[i+1][0]) == 1:
                curr = cnt[i][1]+cnt[i+1][1]
                maxx=max(maxx,curr)
        return maxx