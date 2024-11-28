class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.maxVotes = -1
        self.leader = None
        self.count = {}
        self.leaders = []

        for p in persons:
            self.count[p] = self.count.get(p, 0) + 1

            if self.count[p] >= self.maxVotes:
                self.maxVotes = self.count[p]
                self.leader = p
            
            self.leaders.append(self.leader)

    def findTimeIdx(self, time):
        target = time
        values = self.times
        l = 0
        r = len(values) - 1
        nearestPrev = -1


        while l <= r:
            m = l + (r - l) // 2

            if values[m] > target:
                r = m - 1
            elif values[m] < target:
                nearestPrev = m
                l = m + 1
            else:
                return m
        
        return nearestPrev



    def q(self, t: int) -> int:
        idx = self.findTimeIdx(t)
        return self.leaders[idx]

        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
