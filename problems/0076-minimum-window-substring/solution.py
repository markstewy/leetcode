class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""
        
        scount = {}
        tcount = {}
        for c in t:
            tcount[c] = tcount.get(c, 0) + 1

        matches = 0
        needed = len(tcount)
        minlen = float("infinity")
        minl, minr = -1, -1

        
        l = 0
        for r in range(len(s)):
            c = s[r]
            scount[c] = scount.get(c, 0) + 1
            if c in tcount and scount[c] == tcount[c]:
                matches += 1

            while matches >= needed:
                if r - l + 1 < minlen:
                    minlen = r - l + 1
                    minl = l
                    minr = r

                c = s[l]
                scount[c] -= 1
                if c in tcount and scount[c] == tcount[c] - 1:
                    matches -= 1
                l += 1

        return s[minl : minr + 1]
            
            

