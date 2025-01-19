class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        solution = []
        cash = [0, 0, 0]
        for b in bills:
            ans = self.hasChange(b, cash)
            if not ans[0]:
                return False
            else:
                cash = ans[1]
                print(cash)
        
        return True


    def hasChange(self, pmt: int, cash: List[int]) -> tuple:
        changeAmt: int = pmt - 5

        if pmt == 5:
            cash[0] += 1
        if pmt == 10:
            cash[1] += 1
        if pmt == 20:
            cash[2] += 1

        priorCash = cash
        while changeAmt > 0:
            progress = False
            if changeAmt >= 20 and cash[2] > 0:
                changeAmt -= 20
                cash[2] -= 1
                progress = True
            if changeAmt >= 10 and cash[1] > 0:
                changeAmt -= 10
                cash[1] -= 1
                progress = True
            if changeAmt >= 5 and cash[0] > 0:
                changeAmt -= 5
                cash[0] -= 1
                progress = True
            if not progress:
                return((False, [])) # no change solultion found

        return (True, cash)

