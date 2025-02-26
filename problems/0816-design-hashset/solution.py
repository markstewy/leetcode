class MyHashSet:

    def __init__(self):
        self.myset = [None] * 10**6
        
    def add(self, key: int) -> None:
        i = key % len(self.myset)
        self.myset[i] = key

    def remove(self, key: int) -> None:
         i = key % len(self.myset)
         self.myset[i] = None

    def contains(self, key: int) -> bool:
        i = key % len(self.myset)
        return self.myset[i] == key
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
