class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        ans = [-1, -1]
        shortest = float('infinity')

        tCount = {}
        for c in t:
            tCount[c] = tCount.get(c, 0) + 1
        
        have = 0
        need = len(tCount)

        window = {}
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            
            if c in tCount and tCount[c] == window[c]:
                have += 1

            while have >= need:
                if (r - l + 1) < shortest:
                    shortest = min(shortest, r - l + 1)
                    ans = [l, r]

                window[s[l]] -= 1

                if s[l] in tCount and tCount[s[l]] - 1 == window[s[l]]:
                    have -= 1

                l += 1
                
        if shortest == float('infinity'):
            return ""
        
        l = ans[0]
        r = ans[1]
        return s[l : r + 1]
        


