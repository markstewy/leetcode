class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]

        for sell in prices:
            profit = sell - buy
            maxProfit = max(maxProfit, profit)

            if sell < buy:
                buy = sell
        
        return maxProfit
