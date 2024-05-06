class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        b = float('infinity')

        for s in prices:
            profit = max(0, s - b)
            mp = max(mp, profit)
            if s < b:
                b = s
        
        return mp
