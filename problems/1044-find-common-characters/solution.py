class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        mergedCount = Counter(words[0])

        for word in words:
            wordCount = Counter(word)
            commonLetters = wordCount.keys() & mergedCount.keys()

            mergedCount = {
                key: min(wordCount[key], mergedCount[key])
                for key in commonLetters
            }
        
        ans = []

        for l, cnt in mergedCount.items():
            for _ in range(cnt):
                ans.append(l)
        
        return ans

