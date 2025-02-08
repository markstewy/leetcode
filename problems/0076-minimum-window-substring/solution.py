class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        minl, minr = 0, float("infinity")
        tcount = Counter(t)
        scount = {}
        needed = len(tcount.keys())
        matches = 0

        l = 0
        for r in range(len(s)):
            c = s[r]
            scount[c] = scount.get(c, 0) + 1

            if c in tcount and tcount[c] == scount[c]:
                matches += 1
            
            while matches >= needed:
                if (r - l) < (minr - minl):
                    print("hit")
                    minr = r
                    minl = l
                    print(f"minl: {minl}.   minr: {minr}")
                c = s[l]
                scount[c] -= 1

                if c in tcount and tcount[c] == scount[c] + 1:
                    matches -= 1
                l += 1

        if minr == float("infinity"):
            return ""
        return s[minl: minr + 1] 
        

