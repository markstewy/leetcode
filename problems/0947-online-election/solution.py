class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        count = {}
        leader = None
        leaderCount = 0
        self.leaderRecord = []
        self.times = times

        for p in persons:
            count[p] = count.get(p, 0) + 1
            if count[p] >= leaderCount:
                leader = p
                leaderCount = count[p]
            self.leaderRecord.append(leader)

    def q(self, t: int) -> int:
        l = 0
        r = len(self.times) - 1
        closestPrev = None

        while l <= r:
            m = l + (r - l) // 2
            if self.times[m] > t:
                r = m - 1
            elif self.times[m] <= t:
                l = m + 1
                closestPrev = m
        
        return self.leaderRecord[closestPrev]




# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
