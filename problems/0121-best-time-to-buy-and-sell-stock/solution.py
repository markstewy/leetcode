class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0

        l = 0

        for r in range(len(prices)):
            mp = max(mp, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            
        return mp
