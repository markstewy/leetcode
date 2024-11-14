class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []

        def helper(l, r, s):
            if len(s) == n * 2:
                self.ans.append(s)
                return
            
            if l < n: # add left
                helper(l + 1, r, s + "(")
            if l > r: # add right
                helper(l, r + 1, s + ")")
        
        helper(1, 0, "(")
        return self.ans
            
