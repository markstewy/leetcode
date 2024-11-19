class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        count = {}
        maxVotes = 0
        leader = ""
        self.leaders = []
        self.times = times

        for p in persons:
            count[p] = count.get(p, 0) + 1
            if count[p] >= maxVotes:
                maxVotes = count[p]
                leader = p
            self.leaders.append(leader)


    def q(self, t: int) -> int:
        times = self.times
        l = 0
        r = len(times) - 1
        nearestPrev = -1
        target = t
        
        while l <= r:
            m = l + (r - l) // 2

            if times[m] < target:
                nearestPrev = m
                l = m + 1
            elif times[m] > target:
                r = m - 1
            else:
                return self.leaders[m]
        
        return self.leaders[nearestPrev]

        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
