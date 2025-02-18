class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.votes = list(zip(times, persons))
        self.leaders = []

        voteCount = {}
        leader = None
        leaderCount = 0

        for t, p in self.votes:
            voteCount[p] = voteCount.get(p, 0) + 1
            if voteCount[p] >= leaderCount:
                leaderCount = voteCount[p]
                leader = p
            self.leaders.append([t, leader])

        print(self.leaders)

    def q(self, t: int) -> int:
        l = 0
        r = len(self.leaders) - 1
        closestPrev = self.leaders[-1][1]

        while l <= r:
            m = l + (r - l) // 2

            if t >= self.leaders[m][0]:
                closestPrev = self.leaders[m][1]
                l = m + 1
            else:
                r = m - 1
        
        return closestPrev
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
