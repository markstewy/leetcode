class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0

        buy = prices[0]
        for sell in prices:
            profit = sell - buy
            mp = max(profit, mp)
        
            if sell < buy:
                buy = sell
            
        return mp
