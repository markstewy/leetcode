class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rtl = []
        ltr = []

        mn = float("infinity")
        for p in prices:
            mn = min(mn, p)
            ltr.append(mn)
        
        mx = -float('infinity')
        for i in range(len(prices) - 1, -1, -1):
            mx = max(mx, prices[i])
            rtl.append(mx)
        rtl.reverse()

        profits = [rtl[i] - ltr[i] for i in range(len(prices))]

        return max(profits)
