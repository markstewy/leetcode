class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        hoursTaken = 0
        l = 1 # min bananas per hour
        r = max(piles)  # max bananas per hour
        slowestCompletionSpeed = None

        while l <= r:
            m = l + (r - l) // 2
            bph = m

            hoursTaken = 0
            for p in piles:
                hoursTaken += math.ceil(p / bph)

            if hoursTaken > h: # too slow
                l = m + 1
            elif hoursTaken <= h: # too fast
                r = m - 1
                slowestCompletionSpeed = bph
            
        return slowestCompletionSpeed
