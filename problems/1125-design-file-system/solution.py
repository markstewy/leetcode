class FileSystem:

    def __init__(self):
        self.store = {}
        self.store[""] = ""   

    def createPath(self, path: str, value: int) -> bool:
        paths = path.split("/")
        # print(paths)
        parent = "/".join(paths[:-1])
        newDir = paths[-1]
        fullPath = parent + "/" + newDir

        if parent not in self.store or fullPath in self.store:
            return False
        else:
            self.store[fullPath] = value
            return True


    def get(self, path: str) -> int:
        if path not in self.store:
            return -1
        return self.store[path]
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
