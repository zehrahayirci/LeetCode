class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [1 for i in range(n)]
        for i  in range(1,n):
            for j in range(n-i,n):
                if nums[j]>nums[n-i-1]:
                    cursum = 1+dp[j]
                    dp[n-i-1]=max(cursum,dp[n-i-1])
        return max(dp)
            