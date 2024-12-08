class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        mergedCount = Counter(words[0])

        for w in words:
            wCount = Counter(w)
            commonKeys = wCount.keys() & mergedCount.keys()
           
            mergedCount = {
                key: min(wCount[key], mergedCount[key])
                for key in commonKeys
            }
        
        ans = []
        for c, cnt in mergedCount.items():
            for _ in range(cnt):
                ans.append(c)
        
        return ans
