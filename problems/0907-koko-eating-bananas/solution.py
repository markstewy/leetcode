class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 # slowest k
        r = max(piles) # fastest k
        slowestCompletionK = r

        while l <= r:
            mk = l + (r - l) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p / mk) # dc
            
            if hours <= h:
                slowestCompletionK = min(mk, slowestCompletionK)
                r = mk - 1
            if hours > h:
                l = mk + 1
        
        return slowestCompletionK
