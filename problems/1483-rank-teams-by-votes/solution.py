class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        candidates = {}

        for c in votes[0]:
            candidates[c] = [0] * len(votes[0])
        
        for vote in votes:
            for place, name in enumerate(vote):
                candidates[name][place] -= 1
        
        finalTally = list(candidates.items())
        finalTally.sort(key=lambda x : (x[1], x[0]))
    
        ans = ""

        for c in finalTally:
            ans += c[0]
        
        return ans
