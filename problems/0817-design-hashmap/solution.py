class MyHashMap:

    def __init__(self):
        self.size = 10**4
        self.arr = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        idx = key % self.size
        kvs = self.arr[idx]
        valueSet = False

        for i, pair in enumerate(kvs):
            if pair[0] == key:
                kvs[i][1] = value
                valueSet = True
        
        if not valueSet:
            kvs.append([key, value])
        

    def get(self, key: int) -> int:
        idx = key % self.size
        kvs = self.arr[idx]
        value = None

        for k, v in kvs:
            if key == k:
                value = v
            
        return value if value != None else -1


    def remove(self, key: int) -> None:
        idx = key % self.size
        kvs = self.arr[idx]
        
        for i, pair in enumerate(kvs):
            if pair[0] == key:
                del kvs[i]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
