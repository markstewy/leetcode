class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l = 1
        r = max(candies)
        maxPileSize = 0

        while l <= r:
            m = l + (r - l) // 2


            kidCount = 0
            for p in candies:
                kidCount += p // m
            
            if kidCount >= k:
                maxPileSize = max(maxPileSize, m)
                l = m + 1
            else:
                r = m - 1
        
        return maxPileSize
