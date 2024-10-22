class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def helper(s, lCount, rCount):
            if len(s) == n * 2:
                ans.append(s)
                return
            
            if lCount > rCount:
                sNext = s + ")"
                helper(sNext, lCount, rCount + 1)
            if lCount < n:
                sNext = s + "("
                helper(sNext, lCount + 1, rCount)

        helper("(", 1, 0)

        return ans
