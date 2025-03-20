class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        count = 0

        for i in range(len(word)):
            if word[i] in "aeiou":
                j = i
                while j < len(word) and word[j] in "aeiou":
                    if len(set(word[i:j+1])) == 5:
                        count += 1
                    j += 1
    
        return count
