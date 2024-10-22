class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        signs = "-+/*"

        def strToInt(n):
            sign = 1
            if n[0] == "-":
                sign = -1
            n = n.lstrip("-")
            return int(n) * sign

        for n in tokens:
            if n not in signs:
                stack.append(strToInt(n))
            else:
                r = stack.pop()
                l = stack.pop()
                if n == "+":
                    stack.append(l + r)
                elif n == "*":
                    stack.append(l * r)
                elif n == "-":
                    stack.append(l - r)
                elif n == "/":
                    sign = 1
                    if l * r < 0:
                        sign = -1
                    stack.append(abs(l) // abs(r) * sign) 
        return stack[-1]



