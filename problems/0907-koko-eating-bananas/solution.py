class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        slowestCompletionSpeed = 0

        while low <= high:
            m = low + (high - low) // 2

            hrs = 0
            for p in piles:
                hrs += math.ceil(p / m)
            
            if hrs <= h:
                slowestCompletionSpeed = m
                high = m - 1
            else:
                low = m + 1
        
        return slowestCompletionSpeed

