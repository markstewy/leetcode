class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0

        for b in bills:
            if b == 5:
                fives += 1
            if b == 10:
                tens += 1

            changeDue = b - 5

            while changeDue >= 10 and tens:
                    changeDue -= 10
                    tens -= 1
            while changeDue >= 5 and fives:
                    changeDue -= 5
                    fives -= 1
            
            if changeDue:
                return False
        
        return True


