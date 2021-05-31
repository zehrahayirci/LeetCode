class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount ==0:
            return 0
        
        dp=[amount+1 for i in range(amount+1)]
        dp[0]=0
        for i in range(0,amount+1):
            for j in coins:
                if j <= i:
                    dp[i]=min(dp[i],1+dp[i-j])
        print(dp)
        if dp[amount]<=amount:
            return dp[amount]
        else:
            return -1
        
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin,amount+1):
                dp[x] = min(dp[x],dp[x-coin]+1)        
        return dp[amount] if dp[amount] != float('inf') else -1 

        