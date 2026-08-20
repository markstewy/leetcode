class Solution:
    def isHappy(self, n: int) -> bool:
        x = set()

        while n not in x:
            print(n)
            x.add(n)
            n = sum(int(char) ** 2 for char in str(n))
            if n == 1:
                print(n)
                return True
        return False 
