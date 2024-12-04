class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]

        for sell in prices:
            maxProfit = max(maxProfit, sell - buy)
            if sell < buy:
                buy = sell
    
        return maxProfit

