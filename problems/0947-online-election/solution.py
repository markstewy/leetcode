class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        votes = list(zip(times, persons))
        votes.sort()

        self.leaders = []
        candidates = {}
        leader = None
        maxVotes = 0

        for v in votes:
            c = v[1]
            t = v[0]
            candidates[c] = candidates.get(c, 0) + 1
            if candidates[c] >= maxVotes:
                maxVotes = candidates[c]
                leader = c
            self.leaders.append([t, leader])


    def q(self, t: int) -> int:
        l = 0
        r = len(self.leaders) - 1
        closestPrev = None

        while l <= r:
            m = l + (r - l) // 2
            if t >= self.leaders[m][0]:
                l = m + 1
                closestPrev = self.leaders[m][1]
            if t < self.leaders[m][0]:
                r = m - 1
        
        return closestPrev


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
