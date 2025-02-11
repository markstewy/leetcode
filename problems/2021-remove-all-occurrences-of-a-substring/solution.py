class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        part = list(part)
        ans = []

        for c in s:
            ans.append(c)
            if len(ans) >= len(part) and ans[-len(part):] == part:
                # AVOID splicing using arrays subsets [], it creates an entire new array copy and hurts performance
                for _ in range(len(part)):
                    ans.pop()
        
        return "".join(ans)

        

        


        
