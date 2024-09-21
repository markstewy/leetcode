class Solution:
    def isPalindrome(self, s: str) -> bool:
        sa = []

        for c in s:
            if c.isalpha() or c.isdigit():
                sa.append(c.lower())
        
        return sa == sa[::-1]
