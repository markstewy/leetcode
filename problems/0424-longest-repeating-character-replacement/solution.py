class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        longest = 0

        for r in range(len(s)):
            c = s[r]
            count[c] = count.get(c, 0) + 1

            while (r - l + 1 - max(count.values())) > k:
                c = s[l]
                l += 1
                count[c] -= 1
            
            longest = max(longest, r - l + 1)
        
        return longest


