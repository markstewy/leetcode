class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leaders = []
        leaderCount = {}
        leader = None
        maxCount = -1

        for p in persons:
            leaderCount[p] = leaderCount.get(p, 0) + 1
            if leaderCount[p] >= maxCount:
                maxCount = leaderCount[p]
                leader = p
            self.leaders.append(leader)

    def getClosestPrevIdx(self, timestamp):
        target = timestamp
        values = self.times

        l = 0
        r = len(values) - 1
        nearestPrev = -1

        while l <= r:
            m = l + (r - l) // 2

            if values[m] < target:
                nearestPrev = m
                l = m + 1
            elif values[m] > target:
                r = m - 1
            else:
                return m
        
        return nearestPrev

    def q(self, t: int) -> int:
        return self.leaders[self.getClosestPrevIdx(t)]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
