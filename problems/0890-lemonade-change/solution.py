class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {
            5: 0, 
            10: 0,
            20: 0
        }

        for b in bills:
            change[b] += 1
            due = b - 5

            while due >= 10 and change[10] > 0:
                due -= 10
                change[10] -= 1
            while due >= 5 and change[5] > 0:
                due -= 5
                change[5] -= 1
            
            if due > 0:
                return False
        
        return True



