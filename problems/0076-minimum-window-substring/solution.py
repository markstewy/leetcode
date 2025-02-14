class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        tcount = Counter(t)
        scount = {}
        lmin, rmin = 0, float("infinity")
        minLen = float("infinity")

        needed = len(tcount.keys())
        matches = 0

        l = 0
        for r in range(len(s)):
            c = s[r]
            scount[c] = scount.get(c, 0) + 1
            
            if c in tcount and tcount[c] == scount[c]:
                matches += 1
        
            while matches >= needed:
                if (r - l + 1) < minLen:
                    minLen = r - l + 1
                    lmin = l
                    rmin = r

                c = s[l]
                l += 1
                scount[c] -= 1

                if c in tcount and tcount[c] == scount[c] + 1:
                    matches -= 1
        
        if rmin == float("infinity"):
            return ""
        return s[lmin : rmin + 1]


            
