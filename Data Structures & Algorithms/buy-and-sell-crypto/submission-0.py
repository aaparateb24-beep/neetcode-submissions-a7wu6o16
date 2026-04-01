class Solution:
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        
        buy = 0
        sell = 1
        max_profit = 0
        
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)
            else:
                buy = sell
            
            sell += 1
        
        return max_profit