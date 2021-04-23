class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_total_profit, min_price_so_far = 0.0, float('inf')
        first_buy_sell_profits = [0] * len(prices)
        for i,price in enumerate(prices):
            min_price_so_far = min(min_price_so_far,price)
            max_total_profit = max(max_total_profit,price-min_price_so_far)
            first_buy_sell_profits[i] = max_total_profit
        
        max_price_so_far = float('-inf')
        for i, price in reversed(list(enumerate(prices[1:], 1))):
            #print(i,price)
            max_price_so_far = max(price, max_price_so_far)
            max_total_profit = max(max_total_profit, max_price_so_far-price + first_buy_sell_profits[i-1])
        return int(max_total_profit)
        