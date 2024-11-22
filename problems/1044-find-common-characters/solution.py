class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        merged = Counter(words[0])
        
        for word in words:
            wordCount = Counter(word)
            commonKeys = wordCount.keys() & merged.keys() # only letters in common

            merged = {
                key: min(wordCount[key], merged[key]) # only if each has duplicate
                for key in commonKeys
            }


        ans = []
        for l, cnt in merged.items():
            for _ in range(cnt):
                ans.append(l)
        return ans

