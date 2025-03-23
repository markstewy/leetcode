class Node:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.l = Node(-1, -1)
        self.r = Node(-1, -1)
        self.l.next = self.r
        self.r.prev = self.l
        self.nodeMap = {}

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        
        node = self.nodeMap[key]
        self.insert(self.cut(node))
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key not in self.nodeMap:
            node = Node(value, key)
            self.nodeMap[key] = node
            self.insert(node)
        else:
            node = self.nodeMap[key]
            node.val = value
            self.insert(self.cut(node))
        
        if len(self.nodeMap) > self.capacity:
            node = self.l.next
            ky = node.key
            self.cut(node)
            del self.nodeMap[ky]        

    def cut(self, node: Node) -> Node:
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        return node
    
    def insert(self, node: Node) -> None:
        node.next = self.r
        node.prev = self.r.prev
        node.prev.next = node
        node.next.prev = node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
