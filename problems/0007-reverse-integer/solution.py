class Solution:
    def reverse(self, x: int) -> int:
        mx = 2**31 - 1
        mn = -(2**31)
        neg = -1 if x < 0 else 1

        if x < 0:
            sArr = list(str(x))[::-1]
            sArr.pop()
        else:
            sArr = list(str(x))[::-1]

        n = int(''.join(sArr)) * neg
        if n > mx or n < mn:
            n = 0
        
        return n
