class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        mp = 0

        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            mp = max(mp, profit)

            if prices[r] < prices[l]:
                l = r
        return mp
