class MinStack:

    def __init__(self):
        self.stack = [] # [{val: number, min: number}]
        

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append({"val": val, "min": min(val, self.stack[-1]["min"])})
        else: 
            self.stack.append({"val": val, "min": val})

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]["val"]

    def getMin(self) -> int:
        return self.stack[-1]["min"] if self.stack else null


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
