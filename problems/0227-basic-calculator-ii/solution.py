class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []

        i = 0
        while i < len(s):
            if s[i].isdigit():
                n = ""
                while i < len(s) and s[i].isdigit():
                    n += s[i]
                    i += 1
                stack.append(int(n))

            if len(stack) >= 3 and stack[-2] == "*":
                b = stack.pop()
                stack.pop()
                a = stack.pop()
                stack.append(a * b)
            if len(stack) >= 3 and stack[-2] == "/":
                b = stack.pop()
                stack.pop()
                a = stack.pop()
                stack.append(a // b)
            if i < len(s):
                stack.append(s[i])
                i += 1
        
        if len(stack) == 1:
            return stack[0]

        ans = 0
        # print(stack)
        for i, d in enumerate(stack):
            if d == "+":
                ans += (stack[i - 1] + stack[i + 1])
                stack[i - 1] = 0
                stack[i + 1] = 0
            if d == "-":
                ans += (stack[i - 1] - stack[i + 1])
                stack[i - 1] = 0
                stack[i + 1] = 0
                
        return ans
            


