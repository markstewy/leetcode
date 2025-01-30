class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.ans = []
        self.digits = digits
        self.dial = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def helper(comb:str, i:int) -> None:
            if i >= len(self.digits):
                if comb:
                    self.ans.append(comb)
                return

            digit = self.digits[i]
            for c in self.dial[digit]:
                helper(comb + c, i + 1)
        
        helper("", 0)
        return self.ans

            
