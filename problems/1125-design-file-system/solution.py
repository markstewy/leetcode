class FileSystem:

    def __init__(self):
        self.store = {}
        self.store[""] = -1

    def createPath(self, path: str, value: int) -> bool:
        parent = "/".join(path.split("/")[:-1])
        newDir = path.split("/")[-1]

        if parent not in self.store or path in self.store:
            return False
        else:
            self.store[path] = value
            return True

    def get(self, path: str) -> int:
        if path not in self.store:
            return -1
        else:
            return self.store[path]
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
