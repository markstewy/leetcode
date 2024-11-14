class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        signs = "+-/*"
        stack = []

        for t in tokens:
            if t not in signs: # t is a number
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
                    if l * r < 0:
                        stack.append(math.ceil(l / r))
                    else:
                        stack.append(l // r)
        return stack[0]
