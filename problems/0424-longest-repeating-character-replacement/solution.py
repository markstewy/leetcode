class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # char -> count
        longest = 0
        maxCharCount = 0
        
        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxCharCount = max(maxCharCount, count[s[r]])

            # while is NOT valid substring
            while (r - l + 1) - maxCharCount > k:
                count[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)
        
        return longest
            


