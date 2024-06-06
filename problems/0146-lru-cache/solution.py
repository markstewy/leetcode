class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lm = Node(0, 0)
        self.rm = Node(0, 0)
        self.lm.next = self.rm
        self.rm.prev = self.lm
        self.cache = {} # val is pointer to the node object

    def insert(self, node: Node):
        l = self.rm.prev
        r = self.rm

        l.next = node
        r.prev = node
        node.prev = l
        node.next = r
    
    def remove(self, node: Node):
        l = node.prev
        r = node.next
        l.next = r
        r.prev = l


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node
        
        if len(self.cache) > self.capacity:
            lru = self.lm.next
            self.remove(lru)
            del self.cache[lru.key]
        
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
