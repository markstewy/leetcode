class FileSystem:

    def __init__(self):
        self.root = {"val": None, "sub": {}}

    def createPath(self, path: str, value: int) -> bool:
        path = path.lstrip("/")
        pathArr = path.split("/")
        newDir = pathArr.pop()

        curr = self.root
        for p in pathArr:
            if p in curr["sub"]:
                curr = curr["sub"][p]
            else:
                return False
        
        if newDir in curr["sub"] and curr["sub"][newDir]["val"] != None:
            return False
        
        if newDir in curr["sub"]:
            curr["sub"][newDir]["val"] = value # so you don't delete exising subdirs
        else:
            curr["sub"][newDir] = { "sub": {}, "val": value }
        return True

    def get(self, path: str) -> int:
        path = path.lstrip("/")
        pathArr = path.split("/")
        curr = self.root

        for p in pathArr:
            if p in curr["sub"]:
                curr = curr["sub"][p]
            else:
                return -1
        
        return -1 if curr["val"] == None else curr["val"]



# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
