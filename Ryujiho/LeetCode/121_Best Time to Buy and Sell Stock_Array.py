class Solution:
    def maxProfit(self,prices):
        left = 0
        max_profit = 0

        for right in range(1, len(prices)):
            if prices[left] < prices[right]: # If there is a profit
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else: # If the right is more lower than the right
                left = right

        return max_profit
