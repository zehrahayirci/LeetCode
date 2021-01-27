class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums[0],nums[1])
        a = self.nocyclerob(nums[:n-1])
        b = self.nocyclerob(nums[1:])
        return max(a,b)
        
    def nocyclerob(sef,nums):
        n = len(nums)
        if len(nums)==2:
            return max(nums[0],nums[1])
        moneys=[0 for i in range(n)]
        moneys[0]=nums[0]
        moneys[1]=max(nums[0],nums[1])
        for i in range(2,n):
            print((nums[i]+moneys[i-2]),nums[i-1])
            moneys[i]=max((nums[i]+moneys[i-2]),moneys[i-1])
        print(moneys)
        return moneys[n-1]
            