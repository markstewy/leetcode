class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for c in s:
            if not stack or c == "(":
                stack.append(c)
            elif c == ")" and stack[-1] == "(":
                stack.pop()
            elif c == ")" and stack[-1] != "(":
                stack.append(c)
            
        
        return len(stack)
            
                
            
