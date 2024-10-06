class Solution:
    def makePalindrome(self, s: str) -> bool:
        errCount = 0

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                errCount += 1
            l += 1
            r -= 1
        
        return errCount <= 2
