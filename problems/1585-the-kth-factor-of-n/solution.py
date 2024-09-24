class Solution:
    def kthFactor(self, n: int, k: int) -> int:

        i = n
        j = 0
        while i  > 0:
            if n % i == 0:
                j += 1
                if j == k:
                    return int(n / i)
            i -= 1
        return -1

