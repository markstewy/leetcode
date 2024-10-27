class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # speed k min 1 and max of max(piles)
        lk = 1
        rk = max(piles)

        k = rk
        while lk <= rk:
            mk = lk + (rk - lk) // 2

            hrs = 0
            for p in piles:
                hrs += math.ceil(p / mk)
            if hrs <= h: # fast enough
                k = min(k, mk)
                rk = mk - 1
            else: # not fast enough
                lk = mk + 1
        return k
            



