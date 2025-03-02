class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        self.charCount = Counter(chars)
        self.length = 0

        def canBeFormed(word):
            wcount = Counter(word)
            
            for ch, count in wcount.items():
                if ch not in self.charCount or wcount[ch] > self.charCount[ch]:
                    return False

            return True

        for w in words:
            if canBeFormed(w):
                self.length += len(w)
        
        return self.length



        
