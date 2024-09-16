class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        substringCache = {} # char: count
        maxSubstringLength = 0

        l = 0
        
        for r in range(len(s)):
            # expand and add to cache
            substringCache[s[r]] = substringCache.get(s[r], 0) + 1

            # shrink and remove from cache (while k exceeded)
            while (r - l + 1) - max(substringCache.values()) > k:
                substringCache[s[l]] -= 1
                l += 1
            
            maxSubstringLength = max(maxSubstringLength, r - l + 1)

        return maxSubstringLength
