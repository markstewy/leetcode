class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        scount = {}
        l = 0
        for r in range(len(s)):
            c = s[r]
            scount[c] = scount.get(c, 0) + 1

            while r - l + 1 - max(scount.values()) > k:
                c = s[l]
                scount[c] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
    
        return longest
