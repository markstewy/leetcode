class Solution:
    def isPalindrome(self, s: str) -> bool:
        strArr = []
        s = s.lower()
        
        for c in s:
            if c.isdigit() or c.isalpha():
                strArr.append(c)
        
        return strArr == strArr[::-1]
