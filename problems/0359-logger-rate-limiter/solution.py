class Logger:

    def __init__(self):
        self.cache = {} #message: timestamp
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        shouldPrint = False
        
        longerThanTen = message in self.cache and timestamp - self.cache[message] >= 10

        if longerThanTen or message not in self.cache:
            self.cache[message] = timestamp
            return True
        else:
            return False



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
