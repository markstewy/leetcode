class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cset = set()
        maxLen = 0

        l = 0
        for r in range(len(s)):
            c = s[r]
            while c in cset:
                cset.remove(s[l])
                l += 1
            cset.add(c)
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen

