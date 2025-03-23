class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if k > sum(candies):
            return 0
        
        l = 1
        r = max(candies)
        maxPileSize = 0

        while l <= r:
            m = l + (r - l) // 2

            # if all kids get candies make pile bigger
            kidCount = 0
            for c in candies:
                kidCount += c // m
            
            if kidCount >= k:
                maxPileSize = m
                l = m + 1 # enough for each kid, increase pile size
            else:
                r = m - 1 # not enought decrease pile size
        
        return maxPileSize
