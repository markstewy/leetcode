class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        mp = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            mp = max(mp, profit)

            if prices[r] < prices[l]:
                l = r
            
            r += 1
        return mp


