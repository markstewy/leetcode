class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def helper(s, l, r):
            # base case
            if len(s) == 2 * n:
                ans.append(s)
                return
            
            if l > r:
                helper(s + ")", l, r + 1)
            if l < n:
                helper(s + "(", l + 1, r)
        
        helper("(", 1, 0)

        return ans



