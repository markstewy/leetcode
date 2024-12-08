class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lk = 1
        rk = max(piles)
        completedSpeed = -1

        while lk <= rk:
            mk = lk + (rk - lk) // 2

            hrs = 0
            for p in piles:
                hrs += math.ceil(p / mk)

            if hrs <= h: # fast enough try slower
                completedSpeed = mk
                rk = mk - 1
            elif hrs > h: # too slow, try faster
                lk = mk + 1

        return completedSpeed
