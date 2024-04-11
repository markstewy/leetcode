class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): 
            return ""

        tCount, window = {}, {}

        for i in range(len(t)):
            tCount[t[i]] = tCount.get(t[i], 0) + 1
        
            # have is the number of chars completely included in the window (inluding any duplicates)
            # need is the total number of unique chars in t
            have = 0
            need = len(tCount)
            sub = [-1, -1]
            subLen = float('infinity')

        # sliding window, expand r until all chars
        # move up l while all chars
        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get((s[r]), 0) + 1
            if s[r] in tCount and window[s[r]] == tCount[s[r]]:
                have += 1

            while have == need:
                if r - l + 1 < subLen:
                    subLen = r - l + 1
                    sub = [l, r]
                
                window[s[l]] -= 1
                if s[l] in tCount and window[s[l]] == tCount[s[l]] - 1:
                    have -= 1
                l += 1
                
        left = sub[0]
        right = sub[1]

        if subLen == float('infinity'):
            return ""

        return s[left : right + 1]


        
