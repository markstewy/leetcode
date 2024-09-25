class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cSet = set()
        ml = 0

        l = 0
        for r in range(len(s)):
            while s[r] in cSet:
                cSet.remove(s[l])
                l += 1
                
            cSet.add(s[r])
            ml = max(ml, r - l + 1)
        
        return ml






        
