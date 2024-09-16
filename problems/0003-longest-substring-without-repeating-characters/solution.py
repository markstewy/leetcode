class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = set()

        l = 0
        r = 0
        maxLength = 0

        while r < len(s):
            while s[r] in cache:
                cache.remove(s[l])
                l += 1

            cache.add(s[r])
            maxLength = max(maxLength, r - l + 1)

            r += 1
        return maxLength

