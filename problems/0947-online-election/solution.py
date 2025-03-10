class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.votes = list(zip(times, persons))        
        self.votes.sort()

        leader = ""
        leaderCount = 0
        count = {}
        self.leaders = []

        for t, p in self.votes:
            count[p] = count.get(p, 0) + 1
            if count[p] >= leaderCount:
                leader = p
                leaderCount = count[p]
                self.leaders.append([t, leader])
        print(self.leaders)

             
    def q(self, t: int) -> int:
        l = 0
        r = len(self.leaders) - 1
        closestPrev = self.leaders[0]

        while l <= r:
            m = l + (r - l) // 2

            if self.leaders[m][0] <= t:
                closestPrev = self.leaders[m]
                l = m + 1
            else:
                r = m - 1
        
        return closestPrev[1]





        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
