class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        scount = {}
        maxLen = 0

        l = 0
        for r in range(len(s)):
            c = s[r]
            scount[c] = scount.get(c, 0) + 1

            while r - l + 1 - max(scount.values()) > k:
                c = s[l]
                scount[c] -= 1
                l += 1
            
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen
