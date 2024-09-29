class Solution:
    def isValid(self, s: str) -> bool:
        openToClosed = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        if s[0] not in openToClosed:
            return False


        stack = []
        for c in s:
            if c in openToClosed:
                stack.append(openToClosed[c])
            elif stack and c == stack[-1]:
                stack.pop()
            else:
                return False
                     
        return len(stack) == 0
