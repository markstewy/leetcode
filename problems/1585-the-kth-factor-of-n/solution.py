class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []

        for i in range(1, n + 1):
            print(i)
            if n % i == 0:
                factors.append(i)
                if len(factors) == k:
                    return factors.pop()
        return -1
