class FileSystem:

    def __init__(self):
        self.paths = {
            "": -1
        }

    def createPath(self, path: str, value: int) -> bool:
        parent = "/".join(path.split("/")[:-1])

        if path in self.paths or parent not in self.paths:
            return False
        else:
            self.paths[path] = value
            return True
        

    def get(self, path: str) -> int:
        if path in self.paths:
            return self.paths[path]
        else:
            return -1
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
