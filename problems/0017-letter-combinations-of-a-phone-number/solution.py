class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        dial = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        def helper(sub: [str], i: int):
            if i >= len(digits):
                ans.append("".join(sub)) if sub else None
                return
            
            for c in dial[digits[i]]:
                sub.append(c)
                helper(sub, i + 1)
                sub.pop() 

        helper([], 0)
        return ans 
            
