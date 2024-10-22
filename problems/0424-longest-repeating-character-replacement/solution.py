class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxLength = 0

        l = 0
        for r in range(len(s)):
            # add r
            count[s[r]] = count.get(s[r], 0) + 1

            while (r - l + 1) - max(count.values()) > k:
                # move up l while more than 2 letters or both letters greater than k
                count[s[l]] -= 1
                l += 1
            
            maxLength = max(maxLength, r - l + 1)
        
        return maxLength

