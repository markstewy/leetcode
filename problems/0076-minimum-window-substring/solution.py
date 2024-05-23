class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # expand window to the right check counts and matches

        # while you have enough matches bring up the left and update matches
        # everytime you bring up the left also check for length of sub and record l,r index

        # look for t within s
        tcount = {}
        swin = {}

        for c in t:
            tcount[c] = tcount.get(c, 0) + 1


        matches = 0
        need = len(tcount.keys())
        l = 0
        minSub = float('infinity')
        minr = -1
        minl = -1

        for r in range(len(s)):
            c = s[r]
            swin[c] = swin.get(c, 0) + 1

            if c in tcount and tcount[c] == swin[c]:
                matches += 1

            while matches >= need:
                # record new min
                if (r - l + 1) < minSub:
                    minSub = r - l + 1
                    minl = l
                    minr = r

                # move up left pointer
                c = s[l]
                swin[c] -= 1
                
                if c in tcount and tcount[c] == swin[c] + 1:
                    matches -= 1

                l += 1
        
        if minSub == float('infinity'):
            return ""
        return s[minl : minr + 1]
