class FileSystem:

    def __init__(self):
        self.root = {}
        self.root[""] = None
    
    def createPath(self, path: str, value: int):
        p = path.split("/")
        parent = "/".join(p[:-1])
        if path in self.root or parent not in self.root:
            return False

        self.root[path] = value
        return True

    def get(self, path):
        if path in self.root:
            return self.root[path]
        return -1
        

        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
