class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        buy = prices[0]
        sell = 0

        for p in prices:
            sell = p
            profit = sell - buy
            maxP = max(profit, maxP)

            if sell < buy:
                buy = sell
        
        return maxP
