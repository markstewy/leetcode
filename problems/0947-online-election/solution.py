class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.leaders = []

        count = {}
        leader = None
        leaderCount = -1

        for p in persons:
            count[p] = count.get(p, 0) + 1
            if count[p] >= leaderCount:
                leader = p
                leaderCount = count[p]
            
            self.leaders.append(leader)


    def q(self, t: int) -> int:
        target = t
        values = self.times
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
                closestPrev = m
                break
        
        return self.leaders[closestPrev]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
