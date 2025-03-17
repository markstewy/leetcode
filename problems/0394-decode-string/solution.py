class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []

        for c in s:
            stack.append(c)
            if stack[-1] == "]":
                stack.pop()
                sub = ""
                while stack[-1] != "[":
                    sub = stack.pop() + sub
                stack.pop()
                
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                stack.append(sub * int(k))
        
        return "".join(stack)
