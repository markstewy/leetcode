class Solution:
    def isPalindrome(self, s: str) -> bool:
        newArr = []
        s = s.lower()

        for c in s:
            if c.isalpha() or c.isdigit():
                newArr.append(c)
            
        return newArr == newArr[::-1]
