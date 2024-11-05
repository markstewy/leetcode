class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cSet = set()
        longest = 0

        l = 0
        for r in range(len(s)):
            while s[r] in cSet:
                cSet.remove(s[l])
                l += 1
            cSet.add(s[r])
            longest = max(longest, r - l + 1)
        
        return longest
