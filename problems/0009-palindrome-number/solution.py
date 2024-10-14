class Solution:
    def isPalindrome(self, x: int) -> bool:
        sArr = list(str(x))
        return sArr == sArr[::-1]
