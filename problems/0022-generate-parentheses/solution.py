class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []

        def helper(s, lcount, rcount):
            if len(s) == 2 * n:
                self.ans.append(s)
                return
            
            if lcount < n:
                helper(s + "(", lcount + 1, rcount)
            if lcount > rcount:
                helper(s + ")", lcount, rcount + 1)
        
        helper("(", 1, 0)

        return self.ans
