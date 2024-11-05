class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def helper(s, l, r):
            if len(s) == n * 2:
                ans.append(s)
                return
            if l < n:
                helper(s + "(", l + 1, r)
            if r < l:
                helper(s + ")", l, r + 1)
        
        helper("(", 1, 0)
    
        return ans
            
