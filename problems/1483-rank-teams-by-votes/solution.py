class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        # [(2, 3, 1, "B")]
        candidates = {}
        for c in votes[0]:
            candidates[c] = [0] * len(votes[0])
        
        for v in votes:
            idx = 0
            for c in v:
                candidates[c][idx] += 1
                idx += 1
        
        candidatesArr = list(candidates.items())
        candidatesArr.sort(key=lambda x : ([-n for n in x[1]], x[0]))

        return "".join([tpl[0] for tpl in candidatesArr])

