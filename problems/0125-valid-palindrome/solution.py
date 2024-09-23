class Solution:
    def isPalindrome(self, s: str) -> bool:
        sArr = []

        for c in s:
            if c.isalpha() or c.isdigit():
                sArr.append(c.lower())
        
        return sArr == sArr[::-1]
