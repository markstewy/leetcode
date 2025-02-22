class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0

        for bill in bills:
            if bill == 5:
                fives += 1
            if bill == 10:
                tens += 1
            
            change = bill - 5

            while change >= 10 and tens:
                change -= 10
                tens -= 1
            while change >= 5 and fives:
                change -= 5
                fives -= 1
            
            if change:
                return False
        return True
        
            
