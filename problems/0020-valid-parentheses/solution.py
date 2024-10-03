class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        if s[0] not in openToClose:
            return False

        for c in s:
            if c in openToClose:
                stack.append(openToClose[c])
            elif not stack or c != stack[-1]:
                return False
            elif c == stack[-1]:
                    stack.pop()
        
        return len(stack) == 0
                
