class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # char - > count
        maxsub = 0
        # is valid if length of sub - max value in count map <= k

        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            maxsub = max(maxsub, r - l + 1)
        
        return maxsub



        # expand to the right
        # if not valid bring up left until is valid
        # record the valid lengths to keep max (we only need the length not the substr idxs)
