class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # "AABABBA"
        #   l    r
        # valid sub if l - most common char <= k

        subStrCharCount = {} # track the most common char
        longestSub = 0
        l = 0

        for r in range(len(s)):
            #add to counter
            subStrCharCount[s[r]] = subStrCharCount.get(s[r], 0) + 1
            #check if string is valid, if not move left ptr
            while r - l + 1 - max(subStrCharCount.values()) > k:
                subStrCharCount[s[l]] -= 1
                l += 1
            #update longestSub
            subLength = r - l + 1
            longestSub = max(longestSub, subLength)
        return longestSub
