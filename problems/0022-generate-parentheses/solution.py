class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        
        def helper(s, l, r):
            if len(s) == n * 2:
                self.ans.append(s)
                return
            if l < n:
                helper(s + "(", l + 1, r)
            if l > r:
                helper(s + ")", l, r + 1)
        
        helper("(", 1, 0)
        return self.ans
