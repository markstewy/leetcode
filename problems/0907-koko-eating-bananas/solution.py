class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minK = r

        while l <= r:
            k = l + (r - l) // 2
            hrs = 0
            for p in piles:
                hrs += math.ceil(p / k)
            
            if hrs <= h:
                minK = k
                r = k - 1
            elif hrs > h:
                l = k + 1
        
        return minK
                


