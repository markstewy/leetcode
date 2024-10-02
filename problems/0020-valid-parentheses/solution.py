class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = []

        if s[0] not in openToClose:
            return False

        for c in s:
            if c in openToClose:
                stack.append(openToClose[c])
            else:
                if stack and c == stack[-1]:
                    stack.pop()
                else: return False
        
        return len(stack) == 0
