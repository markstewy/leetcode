class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dial = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        ans = []
        
        if digits == "":
            return ans

        def helper(sub, i):
            if i == len(digits):
                ans.append("".join(sub))
                return

            d = digits[i]
            for c in dial[d]:
                sub.append(c)
                helper(sub, i + 1)
                sub.pop()
        
        helper([], 0)
        return ans





