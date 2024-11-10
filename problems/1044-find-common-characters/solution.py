class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        mergedCount = Counter(words[0])

        for word in words:
            wordCount = Counter(word)
            commonKeys = wordCount.keys() and mergedCount.keys()

            mergedCount = {
                key: min(wordCount[key], mergedCount[key])
                for key in commonKeys
            }


        ans = []
        for ch, n in mergedCount.items():
            for _ in range(n):
                ans.append(ch)
        
        return ans
