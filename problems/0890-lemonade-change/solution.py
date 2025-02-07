class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        register = {
            5: 0,
            10: 0,
            20: 0
        }

        for b in bills:
            register[b] += 1
            change = b - 5

            while register[10] and change >= 10:
                change -= 10
                register[10] -= 1
            while register[5] and change >= 5:
                change -= 5
                register[5] -= 1
            
            if change:
                return False
        
        return True
