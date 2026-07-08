class Solution:
    def isHappy(self, n: int) -> bool:
        cacheSet = set()
        while True:
            if n == 1:
                return True
            if n in cacheSet:
                return False
            
            cacheSet.add(n)
            n = sum([int(char) ** 2 for char in str(n)])

