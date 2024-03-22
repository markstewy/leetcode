class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        scrubbed = []

        for c in s:
            if c.isalpha() or c.isdigit():
                scrubbed.append(c)
        
        return scrubbed == scrubbed[::-1]
