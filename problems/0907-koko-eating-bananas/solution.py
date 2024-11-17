class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        kl = 1
        kr = max(piles)
        scs = kr

        while kl <= kr:
            km = kl + (kr - kl) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p / km)
            
            if hours <= h: # fast enough to complete all piles, next try going slower
                scs = min(scs, km)
                kr = km - 1
            elif hours > h: # took too long, try going faster next time
                kl = km + 1
            # don't return if hours exact match because we are rounding hours up and may miss a more optimal km
        
        return scs



