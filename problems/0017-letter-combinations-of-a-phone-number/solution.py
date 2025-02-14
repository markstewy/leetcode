class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        self.ans = []
        self.digits = list(digits)

        if not self.digits:
            return self.ans

        def helper(sub, i):
            if len(sub) == len(self.digits):
                if sub:
                    self.ans.append("".join(sub))
                    return
            
            for c in letters[self.digits[i]]:
                sub.append(c)
                helper(sub, i + 1)
                sub.pop()
        
        helper([], 0)
        return self.ans
            
            

            
                
        

        

