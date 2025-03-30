class MyHashSet:

    def __init__(self):
        self.size = 10**4
        self.arr = [[]] * self.size
        

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.arr[key % self.size].append(key)
        

    def remove(self, key: int) -> None:
        for i, k in  enumerate(self.arr[key % self.size]):
            if k == key:
                del self.arr[key % self.size][i]
        

    def contains(self, key: int) -> bool:
        for k in  self.arr[key % self.size]:
            if k == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
