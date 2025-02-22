class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])
        
        for w in words:
            wCount = Counter(w)

            for c in count.keys():
                if c not in wCount:
                    count[c] = 0
                else:
                    count[c] = min(count[c], wCount[c])
        
        ans = []
        for k, c in count.items():
            for _ in range(c):
                ans.append(k)
        
        return ans
