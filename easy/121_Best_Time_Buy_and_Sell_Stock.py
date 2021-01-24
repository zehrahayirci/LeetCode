class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cur = prices[0]
        profit=-1
        for item in range(1,len(prices)):
            if prices[item] < cur:
                cur = prices[item]
            else:
                profit = max(profit,(prices[item]-cur))
        return max(profit,0)
                