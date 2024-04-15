class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        sArr = []
        for c in s:
            if c.isalpha() or c.isdigit():
                sArr.append(c)
            

        return sArr == sArr[::-1]
