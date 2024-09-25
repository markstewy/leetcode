class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mp = 0
        buy = prices[0]
        for sell in prices:
            profit = sell - buy
            mp = max(mp, profit)
            if sell < buy:
                buy = sell
        return mp

