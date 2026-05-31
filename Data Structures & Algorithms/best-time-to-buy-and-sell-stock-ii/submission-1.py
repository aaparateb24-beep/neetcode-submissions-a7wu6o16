class Solution:
    def maxProfit(self, prices):

        # Total profit earned
        profit = 0

        # Start from second day
        for i in range(1, len(prices)):

            # If today's price is higher than yesterday
            if prices[i] > prices[i - 1]:

                # Take the profit
                profit += prices[i] - prices[i - 1]

        return profit