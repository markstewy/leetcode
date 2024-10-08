class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen = 1
        lmx = 0
        rmx = 1

        if len(s) <= 1:
            return s

        for i in range(0, len(s)):
            # split start
            if i > 0 and i < len(s) -1 and s[i - 1] == s[i + 1]:
                l, r = i - 1, i + 1
                while r < len(s) and l >= 0 and s[l] == s[r]:
                    if r - l + 1 > maxlen:
                        maxlen = r - l + 1
                        lmx = l
                        rmx = r
                    l -= 1
                    r += 1

            # pair start
            if i < len(s) - 1 and s[i] == s[i + 1]:
                l, r = i, i + 1
                while r < len(s) and l >= 0 and s[l] == s[r]:
                    if r - l + 1 > maxlen:
                        maxlen = r - l + 1
                        lmx = l
                        rmx = r
                    l -= 1
                    r += 1

        ans = s[lmx : rmx + 1]
        
        if len(ans) == 2:
            if ans[0] == ans[1]:
                return ans
            else:
                return ans[0]

        return ans
                    

