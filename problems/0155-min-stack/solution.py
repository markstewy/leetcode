class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        mn = self.stack[-1]["mn"] if self.stack else None
        
        if mn == None or val < mn:
            mn = val
        
        self.stack.append({"val": val, "mn":mn})
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]["val"]
        

    def getMin(self) -> int:
        return self.stack[-1]["mn"]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
