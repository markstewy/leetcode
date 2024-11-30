class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        candidates = {}

        for c in votes[0]:
            candidates[c] = [0] * len(votes[0])

        
        for v in votes:
            for i, c in enumerate(v):
                candidates[c][i] -= 1
        
        candidatesArr = list(candidates.items())
        candidatesArr.sort(key=lambda x : (x[1], x[0]))

        ans = ""
        for c in candidatesArr:
            ans += c[0]
        
        return ans

