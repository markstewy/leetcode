class MinStack:

    def __init__(self):
        self.stack = [] # {"min": , "val":}
        

    def push(self, val: int) -> None:
        mn = float("infinity")
        if self.stack:
            mn = min(val, self.stack[-1]["min"])
        else:
            mn = val
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
