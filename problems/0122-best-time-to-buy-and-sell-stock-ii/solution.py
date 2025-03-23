class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        prev = prices[0]
        
        for p in prices:
            if p > prev:
                profit += p - prev
            prev = p
        
        return profit





