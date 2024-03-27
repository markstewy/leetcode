class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        mp = 0
        lowest = prices[0]

        for p in prices:
            lowest = min(lowest, p)
            profit = p - lowest
            mp = max(mp, profit)
        return mp

