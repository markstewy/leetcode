class MinStack(object):

    def __init__(self):
        self.stack = [] # {val: n, min: val}

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.stack:
            minVal = min(val, self.stack[-1]["min"])
        else:
            minVal = val
        self.stack.append({"val": val, "min": minVal})
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]["val"]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1]["min"]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
