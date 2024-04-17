class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mp = 0 # max profit
        l = 0
        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            mp = max(profit, mp)

            if prices[r] < prices[l]:
                l = r
        return mp
