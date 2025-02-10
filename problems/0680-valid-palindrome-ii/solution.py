class Solution:
    def __init__(self):
        self.delCount = 0

    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r and s[l] == s[r]:
            l += 1
            r -= 1
        
        if l >= r:
            return True
        
        remainder1 = s[l + 1 : r + 1]
        remainder2 = s[l : r]
        return remainder1 == remainder1[::-1] or remainder2 == remainder2[::-1]
        
        
            

        
        
            
        
