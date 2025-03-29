class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        prev = prices[0]

        for p in prices:
            if p > prev:
                total += p - prev
            prev = p
        
        return total

