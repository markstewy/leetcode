class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        if s == t:
            return t

        count, win = {}, {}
        # intialize count
        for c in t:
            count[c] = count.get(c, 0) + 1
        
        matches = 0
        needed = len(count.keys())

        minLength = float('inf')
        minl, minr = 0, 0

        l = 0
        for r in range(len(s)): 
            # move up r pointer 
            win[s[r]] = win.get(s[r], 0) + 1
            if s[r] in count and count[s[r]] == win[s[r]]:
                matches += 1
            
            while matches >= needed:
                if minLength > r - l + 1:
                    minLength = r - l + 1
                    minl = l
                    minr = r

                # move up l pointer
                win[s[l]] -= 1
                if s[l] in count and win[s[l]] == count[s[l]] - 1:
                    matches -= 1
                l += 1

        return str(s[minl : minr + 1]) if minLength < float('inf') else  ""

