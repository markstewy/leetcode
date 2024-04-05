class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest = 0
        cache = set()
        l = 0

        for r in range(len(s)):
            while s[r] in cache:
                cache.remove(s[l])
                l += 1
            
            cache.add(s[r])
            longest = max(longest, r - l + 1)

        return longest
