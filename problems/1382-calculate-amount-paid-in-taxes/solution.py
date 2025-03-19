class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        brackets.sort()
        for i in range(len(brackets) -1, 0, -1):
            brackets[i][0] -= brackets[i-1][0]
        total = 0

        for upper, perc in brackets:
            taxable = min(upper, income)
            total += (taxable * (perc/100))
            income -= taxable
            if not income:
                break
        
        return total
            
