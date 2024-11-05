class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for sell in prices:
            profit = max(sell - buy, profit)
            if sell < buy:
                buy = sell
        
        return profit
