class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def helper(s, l, r):
            if l == r == n:
                ans.append(s)
                return
            if l > r and r < n:
                variation = s + ")"
                helper(variation, l, r + 1)
            if l < n:
                variation = s + "("
                helper(variation, l + 1, r)

        helper("(", 1, 0)
        return ans

