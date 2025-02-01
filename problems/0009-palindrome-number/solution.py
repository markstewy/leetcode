class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = [c for c in str(x)]
        return y == y[::-1]


