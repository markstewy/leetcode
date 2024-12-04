class Solution:
    def isPalindrome(self, s: str) -> bool:
        sArr = []
        for c in s:
            if c.isdigit() or c.isalpha():
                sArr.append(c.lower())
    
        return sArr == sArr[::-1]
