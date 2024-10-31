class FileSystem:

    def __init__(self):
        self.root = {} #key: sub name value: {"value":val, [subkeys...]}

    def createPath(self, path: str, value: int) -> bool:
        curr = self.root
        path = path.lstrip("/").rstrip("/").split(("/"))
        newDir = path.pop()
        
        for p in path:
            if p in curr:
                curr = curr[p]
            else:
                return False
        if newDir in curr:
            return False
        
        curr[newDir] = {}
        curr[newDir]["value"] = value
        return True

    def get(self, path: str) -> int:
        curr = self.root
        path = path.lstrip("/").rstrip("/").split(("/"))
        
        for p in path:
            if p in curr:
                curr = curr[p]
            else:
                return -1

        return curr["value"]

        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
