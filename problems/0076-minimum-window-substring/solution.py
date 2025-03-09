class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcount = Counter(t)
        scount = {}
        minWin = float("infinity")
        minl, minr = 0, 0

        matches = 0
        needed = len(tcount.keys())

        l = 0
        for r in range(len(s)):
            print(f"{l}. {r}")
            c = s[r]
            scount[c] = scount.get(c, 0) + 1

            if c in tcount and tcount[c] == scount[c]:
                matches += 1
            # print(matches)
            while matches >= needed:
                # print(f"{matches}.  {needed}")
                if r - l + 1 < minWin:
                    minWin = r - l + 1
                    minr = r
                    minl = l

                c = s[l]
                scount[c] -= 1
                if c in tcount and tcount[c] == scount[c] + 1:
                    matches -= 1
                
                l += 1
        if minWin == float("infinity"):
            return ""
        return s[minl : minr + 1]

