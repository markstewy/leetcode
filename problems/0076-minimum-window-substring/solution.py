class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        sCount, tCount = {}, {}

        for c in t:
            tCount[c] = tCount.get(c, 0) + 1
        
        matches = 0
        needed = len(tCount.keys())

        minLength = float("infinity")
        minl = -1
        minr = -1

        l = 0
        for r in range(len(s)):
            # add r
            c = s[r]
            sCount[c] = sCount.get(c, 0) + 1
            if c in tCount and tCount[c] == sCount[c]:
                matches += 1
            if matches >= needed:
                if (r - l + 1) < minLength:
                    minLength = r - l + 1
                    minl = l
                    minr = r

            # while enough matches bring up l
            while matches >= needed:
                c = s[l]
                sCount[c] -= 1
                if c in tCount and sCount[c] == tCount[c] - 1:
                    matches -= 1
                l += 1

                if matches >= needed:
                    if (r - l + 1) < minLength:
                        minLength = r - l + 1
                        minl = l
                        minr = r
        return s[minl : minr + 1]
