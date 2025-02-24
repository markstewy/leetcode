class FileSystem:

    def __init__(self):
        self.paths = {}
        self.paths[""] = None


    def createPath(self, path: str, value: int) -> bool:
        pathArr = path.split("/")
        parent = "/".join(pathArr[:-1])
        if parent not in self.paths or path in self.paths:
            return False
        else:
            self.paths[path] = value
            return True

    def get(self, path: str) -> int:
        if path not in self.paths:
            return -1
        return self.paths[path]
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
