class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # if it's an int push to the stack
        # if not perform the operation on the ints
        # a, b, c,   for the '-' operation it woudl be b - c (rearrange the pops accordingly)

        stack = []
        for t in tokens:                
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(trunc(b / a))
            else:
                stack.append(int(t))
        
        return stack[0]
