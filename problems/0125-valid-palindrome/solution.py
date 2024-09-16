class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []

        for c in s:
            c = c.lower()
            if c.isalpha() or c.isdigit():
                arr.append(c)

        return arr == arr[::-1]
