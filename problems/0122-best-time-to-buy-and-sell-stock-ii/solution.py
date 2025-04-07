class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = prices[0]
        total = 0

        for p in prices:
            if p > prev:
                total += p - prev
            prev = p
        
        return total

