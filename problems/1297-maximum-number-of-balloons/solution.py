class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        balloonCount = 0

        while True:
            for c in "balloon":
                if c in count and count[c] > 0:
                    count[c] -= 1
                else:
                    return balloonCount
            
            balloonCount += 1
