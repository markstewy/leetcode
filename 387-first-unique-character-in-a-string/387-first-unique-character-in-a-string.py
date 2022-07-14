class Solution:
    def firstUniqChar(self, s: str) -> int:
        myMap = {}
        for c in s:
            myMap[c] = 1 if c not in myMap else myMap[c] + 1
        
        for i, c in enumerate(s):
            if myMap[c] == 1:
                return i
        return -1