class Node:
    def __init__(self, val, key):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.l = Node(-1, "")
        self.r = Node(-1, "")
        self.l.next = self.r
        self.r.prev = self.l

        self.nodeMap = {}

    def get(self, key: int) -> int:
        if key in self.nodeMap:
            self.moveToTop(key)
            return self.nodeMap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            self.moveToTop(key)
            self.nodeMap[key].val = value
        else:
            # create node
            self.nodeMap[key] = Node(value, key)
            node = self.nodeMap[key]
            # append to top of list
            node.prev = self.r.prev
            node.next = self.r
            self.r.prev.next = node
            self.r.prev = node
        while len(self.nodeMap.keys()) > self.capacity:
            self.delete(self.l.next.key)


    def delete(self, key) -> None:
        node = self.nodeMap[key]
        node.next.prev = node.prev
        node.prev.next = node.next
        del self.nodeMap[key]
    
    def moveToTop(self, key) -> None:
        node = self.nodeMap[key]
        # remove the node
        node.next.prev = node.prev
        node.prev.next = node.next

        # add to top of list
        node.prev = self.r.prev
        node.next = self.r
        self.r.prev.next = node
        self.r.prev = node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
