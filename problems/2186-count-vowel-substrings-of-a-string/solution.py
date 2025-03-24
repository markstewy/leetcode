class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        count = 0
        
        for i in range(len(word)):
            vset = set()
            j = i
            while j < len(word) and word[j] in "aeiou":
                vset.add(word[j])
                if len(vset) == 5:
                    count += 1
                j += 1
        
        return count
                

            
