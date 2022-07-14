class Solution:
    def firstUniqChar(self, s: str) -> int:
        myMap = {}
        for c in s:
            myMap[c] = 1 if c not in myMap else myMap[c] + 1
        
        counter = 0
        for c in s:
            if myMap[c] == 1:
                return counter
            counter = counter + 1
        return -1