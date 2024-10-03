class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        signs = "+-?*"
        stack = []

        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif t == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(trunc(b / a))
            else:
                stack.append(int(t))
        
        return stack[0]


