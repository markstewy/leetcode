class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        tcount = Counter(t)
        scount = {}
        minl, minr = None, None
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
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    minl = l
                    minr = r

                c = s[l]
                l += 1
                scount[c] -= 1

                if c in tcount and tcount[c] == scount[c] + 1:
                    matches -= 1
        
        if minl == None:
            return ""
        return s[minl : minr + 1]
                
