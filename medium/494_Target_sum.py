class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if sum(nums) < S or (S+sum(nums)) % 2:
            return 0
        a= (S+sum(nums)) / 2
        dp=[0 for x in range(a+1)]
        dp[0]=1
        for n in nums:
            for i in range(a, n-1, -1):
                dp[i]+=dp[i-n]
            print(dp)
        return dp[a]
        