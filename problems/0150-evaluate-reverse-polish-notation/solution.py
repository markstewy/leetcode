class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "+-*/"

        for c in tokens:
            if c not in operators:
                if c[0] == "-":
                    stack.append(-int(c[1:]))
                else:
                    stack.append(int(c))
            else:
                r = stack.pop()
                l = stack.pop()

                if c == "+":
                    stack.append(l + r)
                if c == "-":
                    stack.append(l - r)
                if c == "*":
                    stack.append(l * r)
                if c == "/":
                    if l * r < 0:
                        stack.append(math.ceil(l / r))
                    else:
                        stack.append(l // r)
        
        return stack[-1]
