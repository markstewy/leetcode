class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leaders = []
        count = {}
        maxVotes = 0
        leader = None

        for p in persons:
            count[p] = count.get(p, 0) + 1
            if count[p] >= maxVotes:
                maxVotes = count[p]
                leader = p
            
            self.leaders.append(leader)
        

    def q(self, t: int) -> int:
        idx = self.findNearestTimeIdx(t)
        return self.leaders[idx]
        

    def findNearestTimeIdx(self, time):
        values = self.times
        target = time
        l = 0
        r = len(values) - 1
        closestPrev = -1

        while l <= r:
            m = l + (r - l) // 2

            if values[m] < target:
                closestPrev = m
                l = m + 1
            elif values[m] > target:
                r = m - 1
            else:
                return m
        
        return closestPrev

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
