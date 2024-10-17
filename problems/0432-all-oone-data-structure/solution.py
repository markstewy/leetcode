# sorted doubly link list with lminhead and rmaxhead

# dict keeps pointer to the node

# if inc/dec shift node right or left

class Node:
    def __init__(self, key):
        self.next = None
        self.prev = None
        self.count = 1
        self.key = key

class AllOne:

    def __init__(self):
        self.lmin = Node(None)
        self.rmax = Node(None)
        self.lmin.count = -float("infinity")
        self.rmax.count = float("infinity")
        self.lmin.next = self.rmax
        self.rmax.prev = self.lmin

        self.dict = {} # key: Node
        self.ans = []

    def inc(self, key: str) -> None:
        # key to access pointer to node and increment value and shift in list
        if key in self.dict:
            self.dict[key].count += 1
            self.sortNode(self.dict[key])
            
        else:
            # insert at left of list (no need to sort, lowest will always be min of 1)
            node = Node(key)
            self.insertRight(self.lmin, node)
            # add to dict
            self.dict[key] = node
        # self.printList()
        
    def dec(self, key: str) -> None:
        # key to access pointer to node and increment value and shift in list
        self.dict[key].count -= 1
        # self.printList()
        if self.dict[key].count == 0:
            self.removeNode(self.dict[key])
            del self.dict[key]
        else:
            self.sortNode(self.dict[key])
        # self.printList()

    def getMaxKey(self) -> str:
        # return value from rmaxhead
        if self.rmax.prev.key:
            self.ans.append(f"getMax: {self.rmax.prev.key}")
            return self.rmax.prev.key
        else:
            return "" # empty list
        
    def getMinKey(self) -> str:
        # return value from lminhead
        if self.lmin.next.key:
            self.ans.append(f"getMin: {self.lmin.next.key}")
            return self.lmin.next.key
        else:
            return "" # empty list
    
    def sortNode(self, node):
        if node.count > node.next.count:
            target = node.next
            while node.count > target.count:
                target = target.next
            # insert to the left of target
            self.removeNode(node)
            self.insertLeft(target, node)
            
        if node.count < node.prev.count:
            target = node.prev
            while node.count < target.count:
                target = target.prev
            # insert to the right of taraget
            self.removeNode(node)
            self.insertRight(target, node)
        # self.printList()
    
    def removeNode(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def insertLeft(self, targetNode, node):
        next = targetNode
        prev = targetNode.prev
        next.prev = node
        prev.next = node
        node.next = next
        node.prev = prev
    
    def insertRight(self, targetNode, node):
        prev = targetNode
        next = targetNode.next
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next
    
    # def printList(self):
    #     x = []
    #     curr = self.lmin
    #     while curr:
    #         x.append(f"key: {curr.key}, count:{curr.count}")
    #         curr = curr.next
    #     print(x)        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
