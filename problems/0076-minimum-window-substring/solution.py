class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        scount, tcount = {}, {}

        for c in t:
            tcount[c] = tcount.get(c, 0) + 1

        matches = 0
        needed = len(tcount.keys())
        minLen = float("infinity")
        minl, minr = -1 , -1

        l = 0
        for r in range(len(s)):
            # add to scount
            c = s[r]
            scount[c] = scount.get(c, 0) + 1

            if c in tcount and scount[c] == tcount[c]:
                matches += 1
            
            # remove left while matches >= needed (also track the new mins here)
            while matches >= needed:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    minl = l
                    minr = r
                
                c = s[l]
                print(scount[c])
                scount[c] -= 1
                if c in tcount and scount[c] == tcount[c] - 1:
                    matches -= 1
                l += 1
        
        return s[minl : minr + 1]


        

