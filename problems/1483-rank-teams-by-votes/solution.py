class Solution:
    def rankTeams(self, votes: List[str]) -> str:

        candidateCount = len(votes[0])
        count = {} # [] size of candidates

        for candidate in votes[0]:
            count[candidate] = [0] * candidateCount # number of potential ranks
        
        for ballot in votes:
            for place, candidate in enumerate(ballot):
                count[candidate][place] += 1
        
        candidateVotes = list(count.items())
        candidateVotes.sort()
        candidateVotes.sort(key=lambda x:x[1], reverse=True)

        ans = ""
        for c in candidateVotes:
            ans += c[0]
        
        return ans

        

