class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        sCount, tCount = {}, {}
        minLength = float("infinity")
        minl, minr = -1, -1

        for c in t:
            tCount[c] = tCount.get(c, 0) + 1
        
        needed = len(tCount)
        matches = 0
        
        l = 0
        for r in range(len(s)):
            # add r
            c = s[r]
            sCount[c] = sCount.get(c, 0) + 1

            if c in tCount and sCount[c] == tCount[c]:
                matches += 1

            # remove l
            while matches >= needed:
                if r - l + 1 < minLength:
                    minLength = r - l + 1
                    minl = l
                    minr = r
                
                c = s[l]
                sCount[c] -= 1
                if c in tCount and sCount[c] == tCount[c] - 1:
                    matches -= 1
                l += 1
        
        return s[minl : minr + 1]
