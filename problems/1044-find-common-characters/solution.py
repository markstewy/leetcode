class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        mainCount = Counter(words[0])

        for word in words: # {"ch": n, "ch2": n2}
            wordCount = Counter(word)
            commonKeys = wordCount.keys() and mainCount.keys()
            mainCount = {
                key: min(wordCount[key], mainCount[key])
                for key in commonKeys
           }

        ans = []
        for ch, n in mainCount.items():
            for _ in range(n):
                ans.append(ch)

        return ans



            
                
            
            
        

        

        
