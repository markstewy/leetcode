class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        scount = {}
        tcount = Counter(t)
        minLen = float("infinity")
        minl, minr = 0, 0

        matches = 0
        needed = len(tcount)

        l = 0
        for r in range(len(s)):
            c = s[r]
            scount[c] = scount.get(c, 0) + 1
            if c in tcount and scount[c] == tcount[c]:
                matches += 1
            
            while matches == needed:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    minr = r
                    minl = l

                c = s[l]
                l += 1
                scount[c] -= 1
                if c in tcount and tcount[c] - 1 == scount[c]:
                    matches -= 1
        
        if minLen == float("infinity"):
            return ""
        
        return s[minl:minr + 1]



