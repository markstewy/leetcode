class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        openToClose = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        if s[0] not in openToClose:
            return False

        stack = []

        for c in s:
            isOpen = c in openToClose
            # if it is a open, add the closed to the stack
            if isOpen:
                stack.append(openToClose[c])
            # while it's a closed, pop it off of the stack
            else:
                if stack and stack[-1] == c:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
                
            # when done the stack should be empty
