class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.leaders = []
        count = {}
        maxVote = 0
        leader = ""

        for i in range(len(persons)):
            p = persons[i]
            count[p] = count.get(p, 0) + 1
            if count[p] >= maxVote:
                maxVote = count[p]
                leader = p

            self.leaders.append({"person": leader, "time": times[i]})
        self.printLeaders()

        
    def q(self, t: int) -> int:
        values = self.leaders
        target = t
        l = 0
        r = len(values) - 1
        closestPrev = -1

        while l <= r:
            m = l + (r - l) // 2

            if values[m]["time"] < target:
                closestPrev = m
                l = m + 1
            elif values[m]["time"] > target:
                r = m - 1
            else:
                return values[m]["person"]
        
        return values[closestPrev]["person"]


    def printLeaders(self):
        s = ""
        for l in self.leaders:
            t = l["time"]
            p = l["person"]
            s += f"p:{p} t: {t},  "
        print(s)



        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
