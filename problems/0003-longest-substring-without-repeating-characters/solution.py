class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0

        cache = set()
        l, r, ml = 0, 0, 1

        while r < len(s):
            while s[r] in cache:
                cache.remove(s[l])
                l += 1
            cache.add(s[r])
            length = r - l + 1
            ml = max(ml, length)

            r += 1
        return ml



