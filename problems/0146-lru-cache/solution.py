class Node:
    def __init__(self, val=None, key=None):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.l = Node()
        self.r = Node()
        self.l.next = self.r
        self.r.prev = self.l

        self.nodeMap = {}
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self.nodeMap:
            node = self.cut(key)
            print(node.val)
            self.insertFront(node)
            return self.nodeMap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.nodeMap:
            self.nodeMap[key] = Node(value, key)
            self.insertFront(self.nodeMap[key])
        else:
            self.nodeMap[key].val = value
            self.insertFront(self.cut(key))
        
        if len(self.nodeMap.keys()) > self.capacity:
            delNode = self.cut(self.l.next.key)
            del self.nodeMap[delNode.key]
        
    def cut(self, key: int) -> Node:
        prev = self.nodeMap[key].prev
        next = self.nodeMap[key].next
        prev.next = next
        next.prev = prev
        
        return self.nodeMap[key]
    
    def insertFront(self, node: Node) -> None:
        prev = self.r.prev
        node.prev = prev
        node.next = self.r
        
        prev.next = node
        self.r.prev = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
