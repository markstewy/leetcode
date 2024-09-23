class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        sCount = {}
        maxL = 0

        l = 0
        for r in range(len(s)):
            # expand right
            sCount[s[r]] = sCount.get(s[r], 0) + 1
            
            # if not valid bring up left
            while (r - l + 1) - max(sCount.values()) > k:
                sCount[s[l]] -= 1
                l += 1
            
            # record valid max length
            maxL = max(maxL, r - l + 1)
            
        
        return maxL

