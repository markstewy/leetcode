class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        candidates = {}

        for c in votes[0]:
            candidates[c] = [0] * len(votes[0])
        
        for v in votes:
            for i, c in enumerate(v):
                candidates[c][i] -= 1
        
        finalCount = list(candidates.items())
        finalCount.sort(key=lambda x : (x[1], x[0]))
    
        ans = ""
        for candidate in finalCount:
            ans += candidate[0]
        
        return ans
