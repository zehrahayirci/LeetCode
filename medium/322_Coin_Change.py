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
        

        