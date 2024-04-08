class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, window = {}, {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1

        have = 0
        need = len(countT)

        sub = [-1, -1]
        subLen = float('infinity')

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if r - l + 1 < subLen:
                    subLen = r - l + 1
                    sub = [l, r]

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] == countT[s[l]] - 1:
                    have -= 1
                l += 1

        l = sub[0]
        r = sub[1] 
        return s[l:r+1] if subLen < float('infinity') else ""


