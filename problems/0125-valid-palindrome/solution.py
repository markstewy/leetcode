class Solution:
    def isPalindrome(self, s: str) -> bool:
        sArr = []

        for c in s:
            c = c.lower()
            if c.isalpha() or c.isdigit():
                sArr.append(c)
        
        return sArr == sArr[::-1]
