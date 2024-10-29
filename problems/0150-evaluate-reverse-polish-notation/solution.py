class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        signs = "+-*/"
        total = 0

        for t in tokens:
            if t not in signs:
                if t[0] == "-":
                    n = int(t[1:]) * -1
                    stack.append(n)
                else:
                    stack.append(int(t))
            else:
                if t == "+":
                    r = stack.pop()
                    l = stack.pop()
                    stack.append(l + r)
                if t == "*":
                    r = stack.pop()
                    l = stack.pop()
                    stack.append(l * r)
                if t == "-":
                    r = stack.pop()
                    l = stack.pop()
                    stack.append(l - r)
                if t == "/":
                    r = stack.pop()
                    l = stack.pop()

                    if l * r < 0:
                        stack.append(math.ceil(l / r))
                    else:
                        stack.append(math.floor(l / r))
        return stack[0]
