class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # len(window) - most common char count <=k: return len(window)
        winCount = {}
        l, r = 0, 0
        ml = 0

        while r < len(s):
            winCount[s[r]] = winCount.get(s[r], 0) + 1

            # while substr is invalid
            while (r - l) + 1 - max(winCount.values()) > k:
                winCount[s[l]] -= 1
                l += 1
            
            ml = max(ml, r - l + 1)
            r += 1
        return ml


