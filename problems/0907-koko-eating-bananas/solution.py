class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        l = 1
        r = piles[-1]

        minSpeed = r

        while l <= r:
            m = l + (r - l) // 2

            hrs = 0
            for p in piles:
                hrs += math.ceil(float(p) / m)
            
            if hrs <= h:
                minSpeed = min(minSpeed, m)
                r = m - 1
            if hrs > h:
                l = m + 1
            
        return minSpeed

