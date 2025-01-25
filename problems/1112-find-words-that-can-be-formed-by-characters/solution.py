class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total = 0

        chars = Counter(chars)
        words = [Counter(word) for word in words]

        for wordCount in words:
            isValid = True
            for letter, count in wordCount.items():
                if letter not in chars or chars[letter] < count:
                    # is not valid word
                    isValid = False
                    break
            if isValid:
                total += sum(wordCount.values())
        
        return total
                
                
