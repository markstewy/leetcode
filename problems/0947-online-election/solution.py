class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        times = list(zip(times, persons))
        times.sort()
        self.leaders = []
        leader = None
        leaderCount = 0
        count = {}
        
        for time, name in times:
            count[name] = count.get(name, 0) + 1
            if count[name] >= leaderCount:
                leaderCount =  count[name]
                leader = name
            self.leaders.append((time, leader))

    def q(self, t: int) -> int:
        l = 0
        r = len(self.leaders) - 1
        closestPrev = self.leaders[-1][1]

        while l <= r:
            m = l + (r - l) // 2

            if self.leaders[m][0] <= t:
                closestPrev = self.leaders[m][1]  
                l = m + 1
            else:
                r = m - 1

        return closestPrev      


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
