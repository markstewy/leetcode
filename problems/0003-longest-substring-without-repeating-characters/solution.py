class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        cache = set()
        longest = 0

        for r in range(len(s)):
            while s[r] in cache:
                cache.remove(s[l])
                l += 1
            cache.add(s[r])
            longest = max(longest, r - l + 1)
        return longest
