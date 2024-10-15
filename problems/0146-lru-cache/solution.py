class Node:
    def __init__(self, key = None, val = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # key: val (pointer to Node)
        self.least = Node()
        self.most = Node()
        self.least.next = self.most
        self.most.prev = self.least
        self.capacity = capacity

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def insert(self, node): # insert to most recently used (right)
        node.next = self.most
        node.prev = self.most.prev
        self.most.prev.next = node
        self.most.prev = node


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            if len(self.cache) == self.capacity:
                leastRecentlyUsedNode = self.least.next
                self.remove(leastRecentlyUsedNode)
                leastRecentlyUsedKey = leastRecentlyUsedNode.key
                del self.cache[leastRecentlyUsedKey]
            
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
