class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        kl = 1
        kr = max(piles)
        slowestFinishingSpeed = kr

        while kl <= kr:
            km = kl + (kr - kl) // 2
            hrs = 0
            for p in piles:
                hrs += math.ceil(p / km)

            if hrs > h: # took more hours than we have
                kl = km + 1 # speed up
            elif hrs <= h: # took less hours than we have
                slowestFinishingSpeed = min(slowestFinishingSpeed, km)
                kr = km - 1 # slow down
        
        return slowestFinishingSpeed
            
