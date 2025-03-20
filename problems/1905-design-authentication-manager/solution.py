class Node:
    def __init__(self, token, exp):
        self.token = token
        self.exp = exp
        self. next = None
        self.prev = None

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.nodes = {}
        self.l = Node("", -float("infinity"))
        self.r = Node("", float("infinity"))
        self.l.next = self.r
        self.r.prev = self.l
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        node = Node(tokenId, currentTime + self.ttl)
        self.insert(node, currentTime + self.ttl)
        self.nodes[tokenId] = node

    def renew(self, tokenId: str, currentTime: int) -> None:
       if tokenId in self.nodes and self.nodes[tokenId].exp > currentTime:
            node = self.nodes[tokenId]
            self.insert(self.cut(node), currentTime + self.ttl)
        
    def countUnexpiredTokens(self, currentTime: int) -> int:
        currNode = self.l.next

        while currNode.exp <= currentTime:
            temp = currNode.next
            self.cut(currNode)
            del self.nodes[currNode.token]
            currNode = temp
        
        return len(self.nodes)

    def cut(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        return node
    
    def insert(self, node, exp):
        node.next = self.r
        node.prev = self.r.prev
        node.next.prev = node
        node.prev.next = node
        node.exp = exp
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
