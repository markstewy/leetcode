class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cSet = set()
        mL = 0

        l = 0
        for r in range(len(s)):
            while s[r] in cSet:
                cSet.remove(s[l])
                l += 1
            cSet.add(s[r])
            mL = max(mL, r - l + 1)
        
        return mL
