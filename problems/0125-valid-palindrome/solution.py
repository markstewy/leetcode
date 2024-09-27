class Solution:
    def isPalindrome(self, s: str) -> bool:
        cArr = []

        for c in s:
            if c.isalpha() or c.isdigit():
                cArr.append(c.lower())
            
        return cArr == cArr[::-1]
