class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []

        def helper(l, r, s):
            if l + r == n * 2:
                self.ans.append(s)
                return
            
            if l > r:
                helper(l, r + 1, s + ")")
            if l < n:
                helper(l + 1, r, s + "(")
        
        helper(1, 0, "(")

        return self.ans

