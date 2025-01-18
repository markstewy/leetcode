class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        minl, minr = 0, len(s)

        scount = {}
        tcount = Counter(t)
        matches = 0
        needed = len(tcount.keys())

        l = 0
        for r in range(len(s)):
            # add new char
            c = s[r]
            scount[c] = scount.get(c, 0) + 1

            if c in tcount and scount[c] == tcount[c]:
                matches += 1

            # remove trailing char
            while matches >= needed:
                if r - l < minr - minl:
                    ans = s[l : r + 1]
                    minl, minr = l, r

                c = s[l]
                scount[c] -= 1
                l += 1

                if c in tcount and tcount[c] - 1 == scount[c]:
                    matches -= 1
        
        return ans
