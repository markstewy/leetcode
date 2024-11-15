class Logger:

    def __init__(self):
        self.msgTimes = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.msgTimes or timestamp - self.msgTimes[message] >= 10:
            self.msgTimes[message] = timestamp
            return True
        else:
            return False

            


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
