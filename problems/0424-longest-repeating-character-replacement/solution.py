class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        count = {} # c -> count

        maxInCount = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxInCount = max(maxInCount, count[s[r]])

            while (r - l + 1) - maxInCount > k:
                count[s[l]] -= 1
                l += 1

                if count[s[l - 1]] + 1 == maxInCount:
                    maxInCount = max(count.values())
            
            longest = max(longest, (r - l + 1))
        
        return longest
            

        

