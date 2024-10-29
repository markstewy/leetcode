class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        candidates = {}
        for c in votes[0]:
            candidates[c] = [0] * len(votes[0])


        for v in votes:
            for i, c in enumerate(v):
                candidates[c][i] += 1
        

        candidates = list(candidates.items())
        candidates.sort()
        candidates.sort(key=lambda x : (x[1]), reverse=True)
        print(candidates)

        ans = ""

        for c in candidates:
            ans += c[0]
        
        return ans
