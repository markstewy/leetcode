class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = set()
        ml = 0

        l = 0

        for r in range(len(s)):
            while s[r] in cache:
                cache.remove(s[l])
                l += 1
            
            cache.add(s[r])
            ml = max(ml, r - l + 1)

        return ml
