class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = []

        for c in s:
            if c in openToClose:
                stack.append(openToClose[c])
            elif stack and c == stack[-1]:
                stack.pop()
            else:
                return False
            
        return not stack
