class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        mn = val
        if self.stack:
            mn = min(mn, self.stack[-1]["min"])
        
        self.stack.append({"val": val, "min": mn})

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]["val"]
        

    def getMin(self) -> int:
        return self.stack[-1]["min"]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
