class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        solution = []

        def backtrack(leftN, rightN):
            # if all chars used push to solution
            # if not all left used, add left
            # if there are more l than r, add r

            if leftN == rightN == n:
                solution.append("".join(stack))
                return
            
            if leftN < n:
                stack.append("(")
                backtrack(leftN + 1, rightN)
                stack.pop()
            
            if leftN > rightN:
                stack.append(")")
                backtrack(leftN, rightN + 1)
                stack.pop()
        
        backtrack(0, 0)
        return solution

