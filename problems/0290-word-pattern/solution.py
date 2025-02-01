class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternToWord = {}
        wordToPattern = {}
        s = s.split(" ")

        if len(s) != len(pattern):
            return False

        for i, c in enumerate(pattern):
            if c in patternToWord and patternToWord[c] != s[i]:
                return False
            if s[i] in wordToPattern and wordToPattern[s[i]] != c:
                return False
            
            patternToWord[c] = s[i]
            wordToPattern[s[i]] = c
        
        return True

