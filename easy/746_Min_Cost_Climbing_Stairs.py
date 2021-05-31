class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n+1) 
        dp[0] = cost[0]
        dp[1] = min((dp[0]+cost[1]),cost[1])
        if n <=2:
            return min(dp[0],dp[1])
        for i in range(2,n):
            dp[i] = min((dp[i-1]+cost[i]),(cost[i]+dp[i-2]))
        #print(dp)
        #print(dp[i])
        return min(dp[i-1],(dp[i]))