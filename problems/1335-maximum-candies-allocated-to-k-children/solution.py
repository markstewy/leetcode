class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        
        candies.sort()
        l = 1
        r = max(candies)
        maxValid = 0

        while l <= r:
            m = l + (r - l) // 2
            pileCount = 0

            for c in candies:
                pileCount += c // m
                if pileCount >= k:
                    break

            if pileCount >= k:
                maxValid = max(maxValid, m)
                l = m + 1
            else:
                r = m - 1
        
        return maxValid
