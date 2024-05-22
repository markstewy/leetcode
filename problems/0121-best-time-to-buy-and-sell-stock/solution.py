class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        b = prices[0]
        
        for p in prices:
            s = p
            profit = s - b
            mp = max(mp, profit)
            
            if s < b: 
                b = s
        
        return mp
