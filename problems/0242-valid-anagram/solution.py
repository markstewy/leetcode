class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        sMap, tMap = {}, {} # n -> count

        for i in range(len(s)):
            print(i)
            sMap[s[i]] = sMap.get(s[i], 0) + 1
            tMap[t[i]] = tMap.get(t[i], 0) + 1
        
        return sMap == tMap
