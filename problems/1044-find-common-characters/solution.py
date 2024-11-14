class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        merged = Counter(words[0])

        for word in words:
            wordCount = Counter(word)
            commonKeys = merged.keys() & wordCount.keys()

            merged = {
                key: min(wordCount[key], merged[key])
                for key in commonKeys
            }
        
        ans = []

        for ch, n in merged.items():
            for _ in range(n):
                ans.append(ch)
        
        return ans
