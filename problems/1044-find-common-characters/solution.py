class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        mergedCount = Counter(words[0])

        for word in words:
            wordCount = Counter(word)
            commonKeys = mergedCount.keys() & wordCount.keys()

            mergedCount = {
                key: min(mergedCount[key], wordCount[key])
                for key in commonKeys
            }
        

        ans = []
        for letter, count in mergedCount.items():
            for _ in range(count):
                ans.append(letter)
        
        return ans
