class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        nArr = []

        for c in s:
            if c.isalpha() or c.isdigit():
                nArr.append(c)
        
        return nArr == nArr[::-1]
