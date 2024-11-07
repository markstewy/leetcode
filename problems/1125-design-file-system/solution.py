
class FileSystem:

    def __init__(self):
        self.root = {"sub": {}}
        

    def createPath(self, path: str, value: int) -> bool:
        path = path.lstrip("/").rstrip("/").split("/")
        newDir = path.pop()

        curr = self.root
        for p in path:
            if p in curr["sub"]:
                curr = curr["sub"][p]
            else:
                return False
                
        if newDir in curr["sub"]:
            return False

        curr["sub"][newDir] = {"val": value, "sub": {}}
        return True

    def get(self, path: str) -> int:
        path = path.lstrip("/").rstrip("/").split("/")

        curr = self.root
        for p in path:
            if p in curr["sub"]:
                curr = curr["sub"][p]
            else:
                return -1

        return curr["val"]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
