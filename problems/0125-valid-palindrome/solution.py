class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for c in s:
            if c.isdigit() or c.isalpha():
                arr.append(c.lower())
        
        return arr == arr[::-1]
