class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        minLength = float("infinity")
        minl, minr = 0, 0
        sCount, tCount = {}, {}

        for i in range(len(t)):
            tCount[t[i]] = tCount.get(t[i], 0) + 1
        
        needed = len(tCount)
        matches = 0

        l = 0
        for r in range(len(s)):
            # add r
            c = s[r]
            sCount[c] = sCount.get(c, 0) + 1
            if c in tCount and sCount[c] == tCount[c]:
                matches += 1

            # if enough matches, bring up l and reset min length if remains valid
            while matches >= needed:
                if (r - l + 1) < minLength:
                    minLength = r - l + 1
                    minl = l
                    minr = r + 1 # right not inclusive in []
                
                c = s[l]
                sCount[c] -= 1
                l += 1
                if c in tCount and sCount[c] == tCount[c] - 1:
                    matches -= 1
        
        if minLength == float("infinity"):
            return ""
        else:
            return s[minl : minr]
            
