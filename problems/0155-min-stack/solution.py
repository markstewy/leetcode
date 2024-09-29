class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        m = min(self.stack[-1]["min"], val) if self.stack else val
        self.stack.append({"val": val, "min":m})

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
