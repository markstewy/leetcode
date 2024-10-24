class FileSystem:

    def __init__(self):
        self.root = {"children": {}, "val": None}
        

    def createPath(self, path: str, value: int) -> bool:
        path = path.lstrip("/").rstrip("/").split("/")
        newDir = path.pop() #!
        
        curr = self.root
        for dir in path:
            if dir in curr["children"]:
                curr = curr["children"][dir]
            else:
                return False
        
        if newDir in curr["children"]:
            return False
        else:
            curr["children"][newDir] = {"val": value, "children": {}}
        
        return True
        

    def get(self, path: str) -> int:
        path = path.lstrip("/").rstrip("/").split("/")
        curr = self.root

        for dir in path:
            if dir in curr["children"]:
                curr = curr["children"][dir]
            else:
                return -1
        
        return curr["val"]
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
