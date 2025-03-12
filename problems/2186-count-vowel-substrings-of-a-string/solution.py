class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        count = 0 
        current = set() 

        for i in range(len(word)):
            current.clear()
            if word[i] in 'aeiou':
                current.add(word[i])
                
                for j in range(i, len(word)):
                    if word[j] not in "aeiou":
                        break                   
                    current.add(word[j])                    
                    if len(current) == 5:
                        count += 1
                        
        return count
