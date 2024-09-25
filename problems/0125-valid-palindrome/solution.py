class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sArr = []
        for c in s:
            if c.isalpha() or c.isdigit():
                sArr.append(c.lower())
        return sArr == sArr[::-1]
