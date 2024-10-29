class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        mn = None
        if not self.stack:
            mn = val
        else:
            mn = min(self.getMin(), val)

        self.stack.append({"min": mn, "val": val})

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
