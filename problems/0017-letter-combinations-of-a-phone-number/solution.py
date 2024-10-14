class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []

        if digits == "": 
            return ans

        numToChars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def helper(numString, variation):
            if numString == "":
                ans.append(variation)
                return
            
            num = numString[0]
            for c in numToChars[num]:
                helper(numString[1:], variation + c)
        
        helper(digits, "")
            
        return ans

            
