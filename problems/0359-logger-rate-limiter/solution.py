class Logger:

    def __init__(self):
        self.msgMap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.msgMap:
            self.msgMap[message] = timestamp + 10
            return True
        
        if self.msgMap[message] > timestamp:
            return False
        else:
            self.msgMap[message] = timestamp + 10
            return True


        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
