class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        slowestCompletion = None

        while l <= r:
            m = l + (r - l) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p / m)

        
            if hours > h: # not fast enough, not completed
                l = m + 1
            elif hours <= h: # fast enough, completed, go slower
                r = m - 1
                slowestCompletion = m
        
        return slowestCompletion
