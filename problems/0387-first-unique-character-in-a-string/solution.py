class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        
        for c in s:
            count[c] = count.get(c, 0) + 1
        
        for i in range(len(s)):
            if s[i] in count and count[s[i]] < 2:
                return i
        return -1
            
