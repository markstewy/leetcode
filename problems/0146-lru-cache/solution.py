class Node():
    def __init__(self, val:int = None, key:str = None, prev = None, next = None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.l = Node()
        self.r = Node()
        self.l.next = self.r
        self.r.prev = self.l
        self.cache = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.moveToFront(key)
        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache: # add to the right
            self.add(key, value)
        else:
            self.remove(key)
            self.add(key, value)
        
        if len(self.cache.keys()) > self.cap:
            self.remove(self.l.next.key)

    def add(self, key:int, value:int) -> None:
            n = Node(value, key)
            self.cache[key] = n
            n.prev = self.r.prev
            n.next = self.r
            self.r.prev.next = n
            self.r.prev = n

    def remove(self, key:int):
            n = self.cache[key]
            n.prev.next = n.next
            n.next.prev = n.prev
            del self.cache[key]

    def moveToFront(self, key):
        n = self.cache[key]
        n.prev.next = n.next
        n.next.prev = n.prev
        
        n.prev = self.r.prev
        n.next = self.r
        
        self.r.prev.next = n
        self.r.prev = n

    
    def plist(self):
        s = ""
        curr = self.l.next
        while curr.next:
            s += f"{curr.val}--> "
            curr = curr.next
        
        print(s)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
