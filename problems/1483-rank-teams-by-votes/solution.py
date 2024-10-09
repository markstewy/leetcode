class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        count = {} # ch: [0, 0, 0]

        for v in votes:
            for i, ch in enumerate(v):
                if ch not in count:
                    count[ch] = [0] * len(v)
                count[ch][i] += 1

        countArr = list(count.items()) # [("A", [0, 0, 0]), ...]
        countArr.sort()
        countArr.sort(key=lambda x: x[1], reverse=True)
        
        ans = ""
        for tup in countArr:
            ans += tup[0]
        
        return ans




            

        

