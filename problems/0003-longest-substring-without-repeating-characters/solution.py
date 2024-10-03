class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cSet = set()
        ml = 0

        l = 0
        for r in range(len(s)):
            while cSet and s[r] in cSet:
                cSet.remove(s[l])
                l += 1
            
            cSet.add(s[r])

            ml = max(ml, r - l + 1)
        return ml


