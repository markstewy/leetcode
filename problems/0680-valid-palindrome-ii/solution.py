class Solution:
    def validPalindrome(self, s: str) -> bool:
        self.replaced = False

        def helper(s):
            l = 0
            r = len(s) - 1

            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    if self.replaced:
                        return False
                    self.replaced = True
                    return (helper(s[l+1:r+1]) or helper(s[l:r]))
            return True
        
        return helper(s)
