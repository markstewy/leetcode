class MyHashMap:

    def __init__(self):
        self.mymap = [None] * 10**6

    def put(self, key: int, value: int) -> None:
        self.mymap[self.hash(key)] = value

    def get(self, key: int) -> int:
        i = self.hash(key)
        if self.mymap[i] == None:
            return -1
        return self.mymap[i]

    def remove(self, key: int) -> None:
        self.mymap[self.hash(key)] = None

    def hash(self, key: int) -> int:
        return key % len(self.mymap)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
