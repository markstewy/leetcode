class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxLen = 0

        l = 0
        for r in range(len(s)):
            c = s[r]
            count[c] = count.get(c, 0) + 1

            while (r - l + 1 - max(count.values())) > k:
                c = s[l]
                count[c] -= 1
                l += 1

            maxLen = max(r - l + 1, maxLen)
        
        return maxLen


