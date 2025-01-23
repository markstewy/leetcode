class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        mainCount = Counter(words[0])
        counts = [Counter(word) for word in words]
        
        for count in counts:
            for letter in mainCount.keys():
                if letter not in count:
                    mainCount[letter] = 0
                else:
                    mainCount[letter] = min(mainCount[letter], count[letter])
        
        ans = []
        print(mainCount)
        for letter, count in mainCount.items():
            for i in range(count):
                ans.append(letter)
        
        return ans




