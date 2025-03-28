class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        maxCompletionSpeed = 0

        while l <= r:
            m = l + (r - l) // 2
            print(m)

            k = 0
            for p in piles:
                k += math.ceil(p / m)
            
            if k <= h:
                maxCompletionSpeed = m
                r = m - 1
            else:
                l = m + 1
        
        return maxCompletionSpeed
