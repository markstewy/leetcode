class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        cache = {}
        mChar = 0
        mCount = 0
        # max occurance - k <= 0 then the substring is valid and record length

        l = 0
        for r in range(len(s)):
            cache[s[r]] = cache.get(s[r], 0) + 1
            if cache[s[r]] > mCount:
                mCount = cache[s[r]]
                mChar = s[r]

            # make substring valid: len - most common char <= number of changes we can make
            while (r - l + 1) - mCount > k:
                cache[s[l]] -= 1
                l += 1

                # if the char we removed was the max count char, we need to 0(n) recalc the max
                if s[l - 1] == mChar:
                    mChar = 0
                    mCount = 0
                    for c , count in cache.items():
                        if count > mCount:
                            mCount = count
                            mChar = c

            
            longest = max(longest, r - l + 1)
        
        return longest



