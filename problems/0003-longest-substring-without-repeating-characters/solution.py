class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cset = set()
        maxLen = 0

        l = 0
        for r in range(len(s)):
            while s[r] in cset:
                cset.remove(s[l])
                l += 1
            
            cset.add(s[r])
            maxLen  = max(maxLen, r - l + 1)
            
        return maxLen
            

