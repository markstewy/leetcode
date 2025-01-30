class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sTot = {}
        tTos = {}

        for i in range(len(s)):
            sc = s[i]
            tc = t[i]

            if sc in sTot and sTot[sc] != tc:
                return False
            elif tc in tTos and tTos[tc] != sc:
                return False
            else:
                sTot[sc] = tc
                tTos[tc] = sc
        
        return True
        
        

