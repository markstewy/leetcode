class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        candidates = {c: [0] * len(votes[0]) for c in votes[0]}

        for v in votes:
            for i, c in enumerate(v):
                candidates[c][i] -= 1
    
        rankings = list(candidates.items())
        rankings.sort(key=lambda x : (x[1], x[0]))
        print(rankings)
        ans = [c[0] for c in rankings]
        return "".join(ans)


