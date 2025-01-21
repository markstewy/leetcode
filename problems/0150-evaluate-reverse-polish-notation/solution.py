class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        signs = "+-*/"

        for t in tokens:
            if t not in signs:
                if t[0] == "-":
                    stack.append(-int(t[1:]))
                else:
                    stack.append(int(t))
            else:
                r = stack.pop()
                l = stack.pop()
                if t == "+":
                    stack.append(l + r)
                if t == "-":
                    stack.append(l - r)
                if t == "*":
                    stack.append(l * r)
                if t == "/":
                    if l * r > 0:
                        stack.append(l // r)
                    else:
                        stack.append(math.ceil(l / r))
        
        return stack[0]
