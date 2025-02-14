class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        parenth = "()"
        s = list(s)

        for i in range(len(s)):
            if s[i] in parenth:
                if s[i] == "(":
                    stack.append(")")
                else:
                    if stack and stack[-1] == ")":
                        stack.pop()
                    else:
                        s[i] = "_"
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] in parenth:
                if s[i] == ")":
                    stack.append("(")
                else:
                    if stack and stack[-1] == "(":
                        stack.pop()
                    else:
                        s[i] = "_"
        
        s = "".join(s).replace("_", "")
        return s
            

