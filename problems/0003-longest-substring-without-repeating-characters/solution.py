class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cSet = set()
        maxLen = 0

        l = 0
        for r in range(len(s)):
            c = s[r]
            
            while c in cSet:
                cSet.remove(s[l])
                l += 1
            
            cSet.add(c)
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen
