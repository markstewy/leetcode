class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        slowestCompletion = float("infinity")

        while l <= r:
            m = l + (r - l) // 2

            hrs = 0
            for p in piles:
                hrs += math.ceil(p / m)
            
            if hrs <= h: # was fast enough (save)
                slowestCompletion = m
                r = m - 1
            elif hrs > h: # took too long, go faster
                l = m + 1
        
        return slowestCompletion
