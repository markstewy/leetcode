class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def helper(s, lCount, rCount):

            # return / break statement
            if len(s) == n * 2:
                ans.append(s)
                return

            # scenarios
            if rCount < lCount:
                helper(s + ")", lCount, rCount + 1)
            if lCount < n:
                helper(s + "(", lCount + 1, rCount)
            
        helper("(", 1, 0)
        return ans
