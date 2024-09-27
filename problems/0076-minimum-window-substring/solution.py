class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        sCount, tCount = {}, {}

        for i in range(len(t)):
            tCount[t[i]] = tCount.get(t[i], 0) + 1
        
        matches = 0
        needed = len(tCount)
        minL = float("infinity")
        minl = -1
        minr = -1

        # for c, count in tCount.items():
        #     if c in sCount and sCount[c] == tCount[c]:
        #         matches += 1


        l = 0
        for r in range(len(s)):
            # add r
            c = s[r]
            sCount[c] = sCount.get(c, 0) + 1
            if c in tCount and tCount[c] == sCount[c]:
                matches += 1
            
            # update min if matches
            if matches >= needed:
                if (r - l + 1) < minL:
                    minL = r - l + 1
                    minl = l
                    minr = r

            # slid up l 
            while matches >= needed:
                c = s[l]
                sCount[c] -= 1
                l += 1

                if c in tCount and sCount[c] == tCount[c] - 1:
                    matches -= 1
                
                if matches >= needed:
                    if (r - l + 1) < minL:
                        minL = r - l + 1
                        minl = l
                        minr = r

            
        return s[minl : minr + 1]
