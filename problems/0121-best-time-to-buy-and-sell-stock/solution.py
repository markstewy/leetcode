class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = prices[0], prices[0]
        maxProfit = 0

        for p in prices:
            sell = p
            profit = sell - buy
            maxProfit = max(maxProfit, profit)
            
            if p < buy:
                buy = p
            
        return maxProfit

