class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        largest = 0

        while r < len(prices):
            largest = max(largest, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
        return largest
