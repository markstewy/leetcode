class Solution:
    def isPalindrome(self, s: str) -> bool:
        newA = []
        s = s.lower()

        for c in s:
            if c.isalpha() or c.isdigit():
                newA.append(c)
        
        return newA == newA[::-1]
