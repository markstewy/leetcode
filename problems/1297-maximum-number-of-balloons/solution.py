class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        charCount = Counter(text)
        charCount["l"] //= 2
        charCount["o"] //= 2
        maxBalloon = float("infinity")

        for c in "balloon":
            maxBalloon = min(maxBalloon, charCount[c])
        
        return maxBalloon



