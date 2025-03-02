class Node():
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None
        self.key = None


class LRUCache:

    def __init__(self, capacity: int):
        self.left = Node()
        self.right = Node()
        self.right.prev = self.left
        self.left.next = self.right

        self.nodeMap = {} # key: node
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        node = self.nodeMap[key]
        self.pasteFront(self.cut(node))
        return node.val


    def put(self, key: int, value: int) -> None:
        if key not in self.nodeMap:
            node = Node(value)
            node.key = key
            self.nodeMap[key] = node
            self.pasteFront(node)
        else:
            node = self.nodeMap[key]
            node.val = value
            self.pasteFront(self.cut(node))
        
        self.trimCache()

    def cut(self, node) -> Node:
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        return node

    def pasteFront(self, node) -> None:
        node.prev = self.right.prev
        node.next = self.right
        node.prev.next = node
        node.next.prev = node

    def trimCache(self):
        while len(self.nodeMap.keys()) > self.capacity:
            node = self.left.next
            key = node.key
            self.cut(node)
            del self.nodeMap[key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
